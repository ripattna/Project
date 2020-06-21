package com.demo

import org.apache.spark.{SparkContext,SparkConf}

object FirstSparkProgram {

  def main(args: Array[String]): Unit = {

    // Creating log level
    import org.apache.log4j._

    Logger.getLogger("org").setLevel(Level.ERROR)
    Logger.getLogger("akka" ).setLevel(Level.ERROR)

    // Creating Conf Object
    val conf=new SparkConf()
    conf.setMaster("local")
    conf.setAppName("FirstSparkProgram")
    val sc=new SparkContext(conf)

    // Creating the RDD
    val rdd1=sc.makeRDD(Array(1,2,3,4,5,6))
    rdd1.collect().foreach(println)
    println("Number of element in RDD:",rdd1.count())

  }
}
