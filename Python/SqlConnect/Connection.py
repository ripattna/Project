from pyspark import SparkContext
from pyspark.sql import HiveContext
import pyspark.sql.functions as F
import datetime
import os
import csv
import sys
import time


def myConcat(*cols):
    concat_columns = []
    for c in cols[:-1]:
        concat_columns.append(F.coalesce(c, F.lit("*")))
        concat_columns.append(F.lit(","))
    concat_columns.append(F.coalesce(cols[-1], F.lit("*")))
    return F.concat(*concat_columns)


sc = SparkContext(appName="Hive_Connect")
sqlContext = HiveContext(sc)
sqlContext.setConf('spark.sql.shuffle.partitions', '50')

try:
    df = df_text = None
    query1 = """
                     SELECT
                        ts_r,
                        trx_date,
                        a_party,
                        charging_id,
                        dialled_apn,
                        event_id
                    FROM (
                        SELECT *,
                            ROW_NUMBER()
                            OVER (PARTITION BY event_date, ORDER BY file_id DESC) as rank
                        FROM base.temp_usage_ocs_chg
                        ) ranked_usage_ocs_chg
                    WHERE ranked_usage_ocs_chg.rank=1;
                """
    df = sqlContext.sql(query1)
    # df_text = df.withColumn("combined", myConcat(*df.columns)).select("combined")
    df.repartition(1).rdd.map(lambda x: ",".join(map(str, x))).saveAsTextFile(
        'hdfs://nameservice1/user/13010840/qtspark_lrf/19GPRS_1')
    # df_text.write.format("text").option("header", "false").mode("append").save(
    # 'hdfs://nameservice1/user/13010840/qtspark_lrf') df.repartition(1000).write.option("header", "false").mode(
    # "append").csv("hdfs://nameservice1/user/13010840/qtspark_lrf")
except Exception as e:
    print("Exception:{0}".format(e))

sc.stop()
