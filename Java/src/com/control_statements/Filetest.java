package com.control_statements;


import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Properties;

public class Filetest {
    public static void main(String[] args) {

        try {
            System.out.println("Working Directory = " + System.getProperty("user.dir"));

            Properties prop = new Properties();
//load properties
            prop.load(new FileInputStream("esp.properties"));
//retrieve properties

            System.out.println(prop.getProperty("dataset"));
            //  logger.info(prop.getProperty("format"));
            //  logger.info("========================================================");
        } catch (FileNotFoundException e) {
// TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }
}


