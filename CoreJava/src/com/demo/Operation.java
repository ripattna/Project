package com.demo;

public class Operation {
    public static void main(String[] args) {

        byte x=10;
        int b=10;
        System.out.println(x++ + ++x); //10+12=22
        System.out.println(b++ + b++); //10+11=21
        System.out.println(x++); //10 (11)
        // System.out.println(++x); //12
        // System.out.println(x--); //12 (11)
        System.out.println(--x); //10

    }
}
