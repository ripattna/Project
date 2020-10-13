package com.demo

import org.apache.spark.sql.types.{StringType, StructField, StructType}
import org.apache.spark.sql.{Row, SparkSession}


object CreateDataFrame {

  def main(args: Array[String]): Unit = {

    // Create SparkSession
    val spark = SparkSession.builder().appName("RDDTransformation").master("local").getOrCreate()
    //val spark: SparkSession = SparkSession.builder().master("local[1]").appName("SparkByExample").getOrCreate()

    // Creating log level
    spark.sparkContext.setLogLevel("WARN")

    import spark.implicits._
    //val columns = Seq("language","users_count")
    val data = Seq(("Java", "20000"), ("Python", "100000"), ("Scala", "3000"))
    val rdd = spark.sparkContext.parallelize(data)

    // Converting RDD to DF (USING toDF())
    //val dfFromRDD1 = rdd.toDF
    val dfFromRDD1 = rdd.toDF("language","users_count")

    println("##########Creating Dataframe from RDD:########################")
    println("Creating dataframe from RDD using toDF:")
    dfFromRDD1.printSchema()
    dfFromRDD1.show()

    // Converting RDD to DF (USING createDataFrame)
    val columns = Seq("language","users_count")
    val dfFromRDD2 = spark.createDataFrame(rdd).toDF(columns: _*)

    println("Creating dataframe from RDD using createDataFrame:")
    dfFromRDD2.printSchema()
    dfFromRDD2.show()

    // From RDD (USING createDataFrame and Adding schema using StructType)
    // convert RDD[T] to RDD[Row]
    val schema = StructType(columns.map(fieldName => StructField(fieldName, StringType, nullable = true)))
    val rowRDD = rdd.map(attributes => Row(attributes._1, attributes._2))
    val dfFromRDD3 = spark.createDataFrame(rowRDD, schema)

    println("Creating dataframe from RDD using createDataFrame and Adding schema using StructType:")
    dfFromRDD3.printSchema()
    dfFromRDD3.show()

    println("##########Creating Dataframe from Data:########################")

    // From Data (USING toDF())
    val dfFromData1 = data.toDF()
    println("Creating dataframe from DATA using toDF:")
    dfFromData1.printSchema()
    dfFromData1.show()

    // From Data (USING createDataFrame)
    var dfFromData2 = spark.createDataFrame(data).toDF(columns: _*)
    println("Creating dataframe from DATA using createDataFrame:")
    dfFromData2.printSchema()
    dfFromData2.show()

    // From Data (USING createDataFrame and Adding schema using StructType)
    import scala.collection.JavaConversions._
    val rowData = data.map(attributes => Row(attributes._1, attributes._2))
    var dfFromData3 = spark.createDataFrame(rowData, schema)

    println("Creating dataframe from DATA using createDataFrame and Adding schema using StructType:")
    dfFromData2.printSchema()
    dfFromData2.show()

  }

}