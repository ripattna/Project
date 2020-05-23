package com.control_statements;

import java.util.Scanner;

public class NumberCheck {
    public static void main(String[] args) {
    Scanner sc =new Scanner(System.in);
        System.out.println("Enter the number to check if it is \"POSITIVE\" or \"NEGAVITE\":");
        int num=sc.nextInt();
        if(num>0)
        {
            System.out.println(num+ " Is POSITIVE number.");
        }
        else if(num<0)
        {
            System.out.println(num+" Is NEGATIVE number.");
        }
        else
        {
            System.out.println(num+" Is ZERO");
        }

    }
}
