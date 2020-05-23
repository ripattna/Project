package com.demo
import org.apache.spark.{SparkConf, SparkContext}
object LoadData {
  def main(args: Array[String]): Unit = {
    import org.apache.log4j._
    //Set the log level to print the error
    Logger.getLogger( "org").setLevel(Level.ERROR)
    val conf = new SparkConf().setAppName("Spark Job for Loading Data").setMaster("local[*]")
    // local[*] will access all core of your machine
    // Create Spark Context
    val sc = new SparkContext(conf)
    sc.setLogLevel("ERROR")
    // Load local file data
    val emp_data = sc.textFile("C:\\Temp\\Input.txt") // It will return a RDD
    // Read the records
    println(emp_data.foreach(println))
  }
}