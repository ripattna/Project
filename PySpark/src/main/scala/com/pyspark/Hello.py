from pyspark import SparkContext,SparkConf

conf = SparkConf().setAppName("appName").setMaster("local")
sc = SparkContext(conf=conf)

myRDD = sc.parallelize([('Jak', 22), ('Viki', 24), ('Jimi', 24), ('Ram', 25), ('Hope', 25), ('Sam', 26)])
myRDDCol = myRDD.collect()
print(myRDDCol)