package com.demo

import org.apache.spark.sql.SparkSession


object RDDtoDF {

  def main(args: Array[String]): Unit = {

    // Create SparkSession
    //val spark = SparkSession.builder().appName("RDDTransformation").master("local").getOrCreate()
    val spark: SparkSession = SparkSession.builder().master("local[1]").appName("SparkByExample").getOrCreate()

    // Creating log level
    spark.sparkContext.setLogLevel("WARN")

    import spark.implicits._
    //val columns = Seq("language","users_count")
    val data = Seq(("Java", "20000"), ("Python", "100000"), ("Scala", "3000"))
    val rdd = spark.sparkContext.parallelize(data)

    // Converting RDD to DF (USING toDF())
    //val dfFromRDD1 = rdd.toDF
    val dfFromRDD1 = rdd.toDF("language","users_count")
    dfFromRDD1.printSchema()
    dfFromRDD1.show()

    // Converting RDD to DF (USING createDataFrame)
    val columns = Seq("language","users_count")
    val dfFromRDD2 = spark.createDataFrame(rdd).toDF(columns: _*)
    dfFromRDD2.printSchema()
    dfFromRDD2.show()

  }

}
