package com.demo

import org.apache.spark.{SparkConf, SparkContext}

object WordCount {

  def main(args: Array[String]): Unit = {

    // Creating Conf Object and SparkContext
    val conf= new SparkConf().setAppName("WordCount").setMaster("local")
    val sc = new SparkContext(conf)

    //Creating log level
    import org.apache.log4j._
    Logger.getLogger("log").setLevel(Level.ERROR)
    sc.setLogLevel("ERROR")

    val readRDD = sc.textFile("C:\\Project\\Files\\Input\\text\\Sample.txt")
    val countRDD = readRDD.flatMap(line => line.split(" ")).map(word => (word,1)).reduceByKey(_+_)
    print(countRDD.count())
    countRDD.saveAsTextFile("C:\\Project\\Files\\Output\\New1")
  }
}
