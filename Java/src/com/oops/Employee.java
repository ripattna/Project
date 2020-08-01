package com.oops;

public class Employee {
    float salary = 40000;
}
class Programmer extends Employee{
    int bonus =10000;

    public static void main(String[] args) {
        Programmer p=new Programmer();
        System.out.println("Programmer salary:"+p.salary);
        System.out.println("Bonus of the Programmer is:"+p.bonus);
    }
}
