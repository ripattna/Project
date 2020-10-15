package com.rdd

import org.apache.log4j.{Level, Logger}
import org.apache.spark.sql.SparkSession

object RddInterviewAskedExercise {

  def main(args: Array[String]): Unit = {

    //Creating SparkSession
    val spark = SparkSession.builder().appName("RddExercise").master("local").getOrCreate()

    //Logger.getLogger("org").setLevel(Level.ERROR)

    //Creating log level
    spark.sparkContext.setLogLevel("WARN")

    val data = List((1,"Ram"),(2,"Sam"),(3,"Hari"),(4,"Rabi"))

    val newRDD = spark.sparkContext.parallelize(data, 3)

    newRDD.take(10).foreach(println)

    println("Partition Size:" +newRDD.partitions.size)
    println("No of Partitions:" +newRDD.getNumPartitions)

    val conv = newRDD.map(x => (x._2.toUpperCase()))
    println("Changing the name to Uppercase")
    conv.take(10).foreach(println)
  }
}
