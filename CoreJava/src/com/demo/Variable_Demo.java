package com.demo;

public class Variable_Demo {
    int data=50; //instance variable
    static int m=100; //static variable
    public void method()
    {
         final int local_variable=90; //local variable
       // return local_variable;
        System.out.println("The local variable value is:" + local_variable);
      }
    public static void main(String[] args) {
        Variable_Demo obj =new Variable_Demo();
        System.out.println("The instance variable value is:" + obj.data);
        System.out.println("The value of static variable is:" + obj.m);
    }

}