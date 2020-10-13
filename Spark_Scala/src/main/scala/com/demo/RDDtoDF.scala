package com.demo

import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.types.{StringType, StructField, StructType}
import org.apache.spark.sql.{DataFrame, Row, SparkSession}
import org.apache.spark.sql.types.StructType

object RDDtoDF {

  def main(args: Array[String]): Unit = {

    // Create SparkSession
    val spark = SparkSession.builder().appName("RDDTransformation").master("local").getOrCreate()

    // Creating log level
    spark.sparkContext.setLogLevel("WARN")

    import spark.implicits._
    val columns = Seq("language","users_count")
    val data = Seq(("Java", "20000"), ("Python", "100000"), ("Scala", "3000"))
    val rdd = spark.sparkContext.parallelize(data)

    // Converting RDD to DF
    //val dfFromRDD1 = rdd.toDF
    val dfFromRDD1 = rdd.toDF("language","users_count")

    dfFromRDD1.printSchema()
    dfFromRDD1.show()

    //val columns = Seq("language","users_count")
    //val dfFromRDD2 = spark.createDataFrame(rdd).toDF(columns:_*)
  }

}
