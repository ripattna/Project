package com.control_statements;

import java.util.Scanner;

public class If_Else_If_Statement {
    public static void main(String[] args) {

     Scanner sc =new Scanner(System.in);
        System.out.println("Enter the Marks:");
        int mark=sc.nextInt();
        if(mark<50)
        {
            System.out.println("FAIL");
        }
        else if(mark >=50 && mark<60)
        {
            System.out.println(" \"D\" GRADE");
        }
        else if(mark>61 && mark<=70)
        {
            System.out.println(" \"C\" GRADE");
        }
        else if(mark>71 && mark<=80)
        {
            System.out.println(" \"B\" GRADE");
        }
        else if(mark>81 && mark<=90)
        {
            System.out.println(" \"A\" GRADE");
        }
        else if(mark>91 && mark<=100)
        {
            System.out.println(" \"A++\" GRADE");
        }
        else {
            System.out.println("INVALID MARK");

        }

    }
}
