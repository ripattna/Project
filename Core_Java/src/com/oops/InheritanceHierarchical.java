package com.oops;

class Animals1 {
    void eat()
    {
        System.out.println("eating");
    }
}
class IndiaDog extends Animals1{
    void bark()
    {
        System.out.println("barking");
    }
}

class IndiaCat extends Animals1{
    void meown()
    {
        System.out.println("meowing");
    }
}
class Inheritance1{
    public static void main(String[] args) {
        IndiaCat c = new IndiaCat();
        c.meown();
        c.eat();
    }
}