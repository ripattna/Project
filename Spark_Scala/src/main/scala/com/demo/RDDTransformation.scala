package com.demo

import org.apache.log4j.{Level, Logger}
import org.apache.spark.{SparkConf, SparkContext}

object RDDTransformation {
  def main(args: Array[String]): Unit = {
    Logger.getLogger( "org").setLevel(Level.ERROR)
    val conf= new SparkConf().setMaster("local").setAppName("RDDTransformation")
    val sc = new SparkContext(conf)
    sc.setLogLevel("ERROR")
    val readRDD=sc.textFile(path ="C:\\Temp\\Sample.txt")
    // readRDD.collect().foreach(println)
    val linesWithSpark = readRDD.filter(line => line.contains("Spark"))
    println("The lines where Spark present in the test:")
    linesWithSpark.collect().foreach(println)
    println("Number of times Spark present in the test:", linesWithSpark.count())
    //val newRDD = readRDD.map(line => line.split(" ").size).reduce((a, b) => if (a > b) a else b)
    sc.stop()
  }
}
