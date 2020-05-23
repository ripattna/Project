package com.control_statements;

import java.util.Scanner;

public class Leap_Year {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the Year to check Leap year or not:");
        int year=sc.nextInt();
        boolean flag=false;
        if(year % 4==0)
        {
            if(year % 100==0)
            {
                if(year % 400==0)
                {
                    flag = true;
                }
                else {
                    flag = false;
                }
            }
            else
            {
                flag = true;
            }
        }
        else
        {
            flag=false;
        }
        if(flag)
            System.out.println(year+ ":is a leap year");
        else
            System.out.println(year+":is not a leap year");
    }
}
