package com.demo;

/*
 * Here we will discuss about different type of Variables available in Java
 */
public class VariablesInJava {

    /*
     * Below variable is INSTANCE VARIABLE as it is outside any method and it is
     * not using STATIC modifier with it. It is using default access modifier.
     * To know more about ACCESS MODIFIER visit appropriate section
     */
    int instanceField;

    /*
     * Below variable is STATIC variable as it is outside any method and it is
     * using STATIC modifier with it. It is using default access modifier. To
     * know more about ACCESS MODIFIER visit appropriate section
     */
    static String staticField;

    public void method() {
        /*
         * Below variable is LOCAL VARIABLE as it is defined inside method in
         * class. Only modifier that can be applied on local variable is FINAL.
         * To know more about access and non access modifier visit appropriate
         * section.
         *
         * Note* : Local variable needs to initialize before they can be used.
         * Which is not true for Static or Instance variable.
         */
        final String localVariable = "Initial Value";
        System.out.println("The local variable value is:" + localVariable);
    }

    public static void main(String args[]) {
        VariablesInJava obj = new VariablesInJava();

        /*
         * Instance variable can only be accessed by Object of the class only as below.
         */
        System.out.println("The value of instance variable is:"+ obj.instanceField);

        /*
         * Static field can be accessed in two way.
         * 1- Via Object of the class
         * 2- Via CLASS name
         */
        System.out.println(obj.staticField);
        System.out.println(VariablesInJava.staticField);
        System.out.println(new VariablesInJava().instanceField);
    }
}