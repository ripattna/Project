package com.demo

import org.apache.spark.{SparkConf,SparkContext}
object ChargeTest {
  def main(args: Array[String]): Unit = {

    //SparkConf for Initialization
    val conf=new SparkConf().setMaster("local").setAppName("ChargeTest")
    val sc=new SparkContext(conf)

    //Creating log level
    import org.apache.log4j._
    Logger.getLogger("log").setLevel(Level.ERROR)
    sc.setLogLevel("ERROR")

    val customerDetails=sc.textFile("C:\\Project\\Files\\Input\\Telkomsel_Feed")
    val myRdd=customerDetails.map(x => x.replace("|","#"))

    //myRDD.collect().foreach(println)
    customerDetails.take(5).foreach(println)
    println("Below the modified value:")
    myRdd.collect.foreach(println)
  }
}
