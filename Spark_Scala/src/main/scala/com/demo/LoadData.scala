package com.demo

import org.apache.spark.{SparkConf, SparkContext}

object LoadData {

  def main(args: Array[String]): Unit = {

    val conf = new SparkConf().setAppName("Spark Job for Loading Data").setMaster("local[*]")
    // local[*] will access all core of your machine
    // Create Spark Context
    val sc = new SparkContext(conf)

    //Set the log level to print the error
    import org.apache.log4j._
    Logger.getLogger( "org").setLevel(Level.ERROR)
    sc.setLogLevel("ERROR")

    // Load local file data
    val emp_data = sc.textFile("C:\\Project\\Files\\Input\\text\\Input.txt") // It will return a RDD
    // Read the records
    println(emp_data.foreach(println))
  }
}