package com.demo

import java.io.File

import org.apache.spark.sql.{Row, SaveMode, SparkSession}

case class Record(key: Int, value: String)

object Hive_Connection {
  def main(args: Array[String]): Unit = {

    //Creating log level
    import org.apache.log4j._

    Logger.getLogger("org").setLevel(Level.ERROR)
    Logger.getLogger("akka" ).setLevel(Level.ERROR)

    // warehouseLocation points to the default location for managed databases and tables
    val warehouseLocation = new File("spark-warehouse").getAbsolutePath

    val spark = SparkSession
      .builder()
      .appName("Spark Hive Example")
      .master("local")
      //.config("spark.sql.warehouse.dir", warehouseLocation)
      //.enableHiveSupport()
      .getOrCreate()

    import spark.sql

    sql("create database if not exists temp_db")
    sql("show databases").show()

  }

}
