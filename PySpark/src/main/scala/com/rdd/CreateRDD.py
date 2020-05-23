from pyspark import SparkContext, SparkConf


class CreteRDD():
    @staticmethod
    def rdd_test():
        try:
            conf = SparkConf().setAppName("appName").setMaster("local")
            sc = SparkContext(conf=conf)

            # Creating a RDD by parallelize a collection

            first_rdd = sc.parallelize(["scala", "java", "python", "ruby", "r", "c", "ansible", "yml", "unix"])
            print("The element of the first RDD is:", first_rdd.collect())
            # print("#######################################################################################")

            # Creating a RDD referencing a data set from a external storage system
            read_rdd = sc.textFile("C:\Project\Files\Input\Input.txt")
            print("The element of the second RDD is:", read_rdd.collect())
            # print("#######################################################################################")

            # Creating a RDD by transforming a existing RDD
            new_rdd = read_rdd.filter(lambda x: 'spark' in x)
            filtered = new_rdd.collect()
            print("This is the filter Spark contains word:", new_rdd.collect())
            sc.stop()
        except:
            print("Enable to create the RDD!")


CreteRDD.rdd_test()
