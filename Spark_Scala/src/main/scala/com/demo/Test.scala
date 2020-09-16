package com.demo

import org.apache.spark.{SparkConf, SparkContext}

object Test {
  def main(args: Array[String]): Unit = {
    import org.apache.log4j._
    Logger.getLogger("org").setLevel(Level.ERROR)
    Logger.getLogger("Akka").setLevel(Level.ERROR)
    //Create Conf Object
    val conf=new SparkConf().
      setMaster("local").
      setAppName("Test")
    //SparkConf to initialize the Spark
    val sc=new SparkContext(conf)
    sc.setLogLevel("ERROR")
    val orderItems=sc.textFile("E:\\Study\\data\\retail_db\\order_items")
    val revenuePerOrder=orderItems.
      map(oi => (oi.split(",")(1).toInt,oi.split(",") (4).toFloat)).
      reduceByKey(_ + _).map(oi =>oi._1 + "," + oi._2)
    //revenuePerOrder.saveAsTextFile(args(2))
    revenuePerOrder.take(15).foreach(println)
  }
}