package com.demo

import org.apache.spark.sql.SparkSession

object Csv_Operation {
  def main(args: Array[String]): Unit = {

    val spark = SparkSession.builder()
      .appName("Spark Hive Example")
      .master("local[1]")
      .getOrCreate()

    //Creating log level
    import org.apache.log4j._
    Logger.getLogger("org").setLevel(Level.ERROR)
    Logger.getLogger("akka").setLevel(Level.ERROR)

    val path ="C:/Project/Files/Input/csv/Sample.csv"
    val df = spark.read
      .option("header","true")
      .csv(path)

    df.printSchema()

    // df.show()

    // df.createGlobalTempView("table")
    df.createOrReplaceTempView("records")
    val sqlDF= spark.sql("select * from records limit 10").show()

  }

}
