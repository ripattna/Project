package com.demo
import org.apache.log4j.{Level, Logger}
import org.apache.spark.{SparkConf, SparkContext}
object ReadingFile {
 def main(args:Array[String]): Unit={
   //Set the log level to print the error
   Logger.getLogger( "org").setLevel(Level.ERROR)
   //Create Conf Object
   val conf=new SparkConf()
   conf.setMaster("local")
   conf.setAppName("ReadingFile")
   //Creating the SparkContext Obj
   val sc=new SparkContext(conf)
   sc.setLogLevel("ERROR")
   val ReadRDD= sc.textFile(path ="C:\\Temp\\Input\\Sample.txt")
  // ReadRDD.take(num = 10).foreach(println)
  // println(ReadRDD.foreach(println))
   println("The count of RDD is:",ReadRDD.count())
 }
}
