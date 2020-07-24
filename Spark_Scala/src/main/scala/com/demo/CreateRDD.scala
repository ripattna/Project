package com.demo
import org.apache.log4j.{Level, Logger}
import org.apache.spark.SparkContext
import org.apache.spark.SparkConf
object CreateRDD {

  def main(args: Array[String]): Unit =
  {
    Logger.getLogger( "org").setLevel(Level.ERROR)
    val conf = new SparkConf().setMaster("local").setAppName("Simple Application")
    val sc = new SparkContext(conf)
    sc.setLogLevel("ERROR")

    //RDD can be created in 3 ways below are the example:
    //Creating a RDD by parallelize a collection
    val firstRDD=sc.parallelize(List("Spark","Hadoop","Kafka"))
    firstRDD.collect().foreach(println)

    //firstRDD.take(10).foreach(println)
    println("The number word in the RDD is:",firstRDD.count())

    //Creating a RDD referencing a data set from a external storage system
    val readRDD=sc.textFile(path ="C:\\Project\\Files\\Input\\text\\Input.txt")
    //readRDD.collect().foreach(println)

    //Creating a RDD by transforming a existing RDD
    val newRDD=readRDD.filter(x=>x.contains("spark"))
    newRDD.collect().foreach(println)

    sc.stop()
  }
}

