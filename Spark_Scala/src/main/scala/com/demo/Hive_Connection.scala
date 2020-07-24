package com.demo

import org.apache.spark.sql.SparkSession

object Hive_Connection {

  def main(args: Array[String]): Unit = {

    val spark = SparkSession.builder().appName("Spark Hive Example").master("local").getOrCreate()

    //Creating log level
    import org.apache.log4j._
    Logger.getLogger("log").setLevel(Level.ERROR)

    //import spark.sql

    spark.sql("create database if not exists temp_db")
    spark.sql("show databases").show()
  }
}
