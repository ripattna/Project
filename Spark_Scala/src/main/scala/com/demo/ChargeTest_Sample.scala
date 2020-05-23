package com.demo
import org.apache.spark.{SparkConf,SparkContext}
object ChargeTest_Sample {
  def main(args: Array[String]): Unit = {
    //Set the log level to print the error
    import org.apache.log4j._
    Logger.getLogger( "org").setLevel(Level.ERROR)
    //Create Conf Object
    val conf=new SparkConf()
    conf.setMaster("local")
    conf.setAppName("ChargeTest_Sample")
    val sc=new SparkContext(conf)
    sc.setLogLevel("ERROR")
    val chargeData=sc.textFile(path ="E:\\Study\\data\\Telkomsel_Feed")
    chargeData.take(num = 10).foreach(println)
  }
}
