import traceback
import importlib
from code import InteractiveConsole
import sys
import socket
import os
import threading
from logging import getLogger

# template used to generate file name
SOCK_FILE_TEMPLATE = '%(dir)s/%(prefix)s-%(pid)d.socket'

log = getLogger(__name__)

class SocketConsole(object):
    '''
    Ported form :eventlet.backdoor.SocketConsole:.
    '''
    def __init__(self, locals, conn, banner=None):  # pylint: diable=W0622
        self.locals = locals
        self.desc = _fileobject(conn)
        self.banner = banner
        self.saved = None

    def switch(self):
        self.saved = sys.stdin, sys.stderr, sys.stdout
        sys.stdin = sys.stdout = sys.stderr = self.desc

    def switch_out(self):
        sys.stdin, sys.stderr, sys.stdout = self.saved

    def finalize(self):
        self.desc = None

    def _run(self):
        try:
            console = InteractiveConsole(self.locals)
            # __builtins__ may either be the __builtin__ module or
            # __builtin__.__dict__ in the latter case typing
            # locals() at the backdoor prompt spews out lots of
            # useless stuff
            import __builtin__
            console.locals["__builtins__"] = __builtin__
            console.interact(banner=self.banner)
        except SystemExit:  # raised by quit()
            sys.exc_clear()
        finally:
            self.switch_out()
            self.finalize()

class _fileobject(socket._fileobject):
    def write(self, data):
        self._sock.sendall(data)

    def isatty(self):
        return True

    def flush(self):
        pass

    def readline(self, *a):
        return socket._fileobject.readline(self, *a).replace("\r\n", "\n")


def make_threaded_backdoor(prefix=None):
    '''
    :return: started daemon thread running :main_loop:
    '''
    socket_file_name = _get_filename(prefix)

    db_thread = threading.Thread(target=main_loop, args=(socket_file_name,))
    db_thread.setDaemon(True)
    db_thread.start()
    return db_thread


def _get_filename(prefix):
    return SOCK_FILE_TEMPLATE % {
        'dir': '/var/run',
        'prefix': prefix,
        'pid': os.getpid(),
    }


def main_loop(socket_filename):
    try:
        log.debug('Binding backdoor socket to %s', socket_filename)
        check_socket(socket_filename)

        sockobj = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sockobj.bind(socket_filename)
        sockobj.listen(5)
    except Exception, e:
        log.exception('Failed to init backdoor socket %s', e)
        return

    while True:
        conn = None
        try:
            conn, _ = sockobj.accept()
            console = SocketConsole(locals=None, conn=conn, banner=None)
            console.switch()
            console._run()
        except IOError:
            log.debug('IOError closing connection')
        finally:
            if conn:
                conn.close()


def check_socket(socket_filename):
    try:
        os.unlink(socket_filename)
    except OSError:
        if os.path.exists(socket_filename):
            raise