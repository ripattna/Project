import pickle
e1=[11,'vijay',222.33]

fp=open('D:\\pythonpgm\\binemp.txt','wb');
pickle.dump(e1,fp)
pickle.dump(e1,fp)
pickle.dump(e1,fp)
pickle.dump(e1,fp)

del e1
fp.close()

fp=open('D:\\pythonpgm\\binemp.txt','rb');
try:
    e1=pickle.load(fp)
    while e1:
        print e1
        e1=pickle.load(fp)
except EOFError:
    print 'no more data'
    

