package com.control_statements;

import java.util.Scanner;

public class If_Else_Statement {
    public static void main(String[] args) {
      int num;
      Scanner console = new Scanner(System.in);
      System.out.println("Enter the number to check even or odd:");
      num=console.nextInt();
        if(num%2==0)
        {
            System.out.println("The number:"+ num +" "+"is even number");
        }
        else{
            System.out.println("The number:"+ num +" "+"is odd number");
        }
    }
}
