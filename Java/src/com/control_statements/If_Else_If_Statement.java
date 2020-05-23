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
            System.out.println(" \"D\" GRANDE");
        }
        else if(mark>60 && mark<70)
        {
            System.out.println(" \"C\" GRANDE");
        }
        else if(mark>70 && mark<80)
        {
            System.out.println(" \"B\" GRANDE");
        }
        else if(mark>80 && mark<90)
        {
            System.out.println(" \"A\" GRANDE");
        }
        else if(mark>90 && mark<100)
        {
            System.out.println(" \"A++\" GRANDE");
        }
        else {
            System.out.println("INVALID MARK");

        }

    }
}
