package com.control_statements;
import java.util.Scanner;
public class If_Statement {
    public static void main(String[] args) {
        int age;
        Scanner console = new Scanner(System.in);
        System.out.println("Enter the person age:");
        age=console.nextInt();
        if (age>=18) {
            System.out.println("Person age is greater than 18");
        }
    }

}
