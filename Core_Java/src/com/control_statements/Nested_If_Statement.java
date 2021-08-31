package com.control_statements;

import java.util.Scanner;

public class Nested_If_Statement
{
    public static void main(String[] args)
    {
      Scanner sc =new Scanner(System.in);
        System.out.println("Enter age to check the eligibility of donate blood:");
        System.out.println("Enter weight to check the eligibility of donate blood:");
        int age=sc.nextInt();
        int weight=sc.nextInt();
        if(age>18)
         {
           if(weight>50)
           {
               System.out.println("You are eligible to donate blood.");
           }
           else
           {
               System.out.println("You are not eligible to donate blood as your weight is less than 50 KG");
           }
        }
        else
        {
            System.out.println("Age must be greater than 18 to donate blood.");
        }

    }
}
