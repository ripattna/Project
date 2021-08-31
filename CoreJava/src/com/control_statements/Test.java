package com.control_statements;

import java.util.Scanner;

public class Test {
    public static void main(String[] args)
    {
     Scanner sc=new Scanner(System.in);
        System.out.println("Enter the first number to add:");
        int num1=sc.nextInt();
        System.out.println("Enter the second number to add:");
        int num2=sc.nextInt();
        int sum=num1+num2;
        System.out.println("The addition of two number is:"+ sum);
    }
}
