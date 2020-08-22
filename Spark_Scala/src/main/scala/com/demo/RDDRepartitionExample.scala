package com.demo

import com.demo.CreateEmptyRDD.rdd
import org.apache.spark.sql.SparkSession

object RDDRepartitionExample extends App{

  val spark:SparkSession = SparkSession.builder()
    .master("local[5]")
    .appName("RDDRepartition")
    .getOrCreate()

  //Creates empty RDD with no partition
  val rdd_1 = spark.sparkContext.emptyRDD // creates EmptyRDD[0]
  println("Num of Partitions: " +rdd_1.getNumPartitions) // returns o partition

  val reparRdd = rdd_1.repartition(4)
  println("re-partition count:"+reparRdd.getNumPartitions)
  //Outputs: "re-partition count:4

  val rdd = spark.sparkContext.parallelize(Range(0,20))
  println("No of Partition:"+rdd.getNumPartitions)
  println("Partition Size:" +rdd.partitions.size)

  /*val rdd1 = spark.sparkContext.parallelize(Range(0,20), 6)
  println("parallelize : "+rdd1.partitions.size)

  rdd1.partitions.foreach(f=> f.toString)
  val rddFromFile = spark.sparkContext.textFile("src/main/resources/test.txt",9)

  println("TextFile : "+rddFromFile.partitions.size)

  rdd1.saveAsTextFile("c:/tmp/partition")
  val rdd2 = rdd1.repartition(4)
  println("Repartition size : "+rdd2.partitions.size)

  rdd2.saveAsTextFile("c:/tmp/re-partition")

  val rdd3 = rdd1.coalesce(4)
  println("Repartition size : "+rdd3.partitions.size)

  rdd3.saveAsTextFile("c:/tmp/coalesce")

   */
}
