package com.demo

import org.apache.log4j.{Level, Logger}
import org.apache.spark.{SparkConf, SparkContext}

object Map_flatMap {
  def main(args: Array[String]): Unit = {


    val conf= new SparkConf().setMaster("local").setAppName("RDDTransformation")
    val sc = new SparkContext(conf)

    Logger.getLogger( "org").setLevel(Level.ERROR)
    sc.setLogLevel("ERROR")

    val x = sc.parallelize(List("spark","rdd","example","sample","kafka"))
    val y = x.map(x=>(x,1))
    y.collect().foreach(print)

    val z = sc.parallelize(List(1,2,3)).flatMap(x=>List(x,x,x))
    z.collect.foreach(println)
    sc.stop()
  }
}
