# Databricks notebook source
# MAGIC %python
# MAGIC sqlContext.setConf("spark.sql.shuffle.partitions", sc.defaultParallelism)

# COMMAND ----------


