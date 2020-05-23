package com.demo
import org.apache.spark.{SparkConf,SparkContext}
object ChargeTest {
  def main(args: Array[String]): Unit = {
    //Creating log level
    import org.apache.log4j._
    Logger.getLogger("log").setLevel(Level.ERROR)
    val conf=new SparkConf()
    conf.setMaster("local")
    conf.setAppName("ChargeTest")
    //SparkConf for Initialization
    val sc=new SparkContext(conf)
    sc.setLogLevel("ERROR")
    val customerDetails=sc.textFile("C:\\Study\\data\\Telkomsel_Feed")
    val myRdd=customerDetails.map(x => x.replace("|","#"))
    //myRDD.collect().foreach(println)
    customerDetails.take(5).foreach(println)
    println("Below the modified value:")
    myRdd.collect.foreach(println)
  }
}
