import findspark
findspark.init()

from pyspark.sql import SparkSession

#Se crea la sesión de spark 
spark = SparkSession.builder \
    .appName("MiAplicacion") \
    .getOrCreate()

#Se crea un data frame 
data = [{"nombre": "Ana", "edad": 30}, {"nombre": "Luis", "edad": 25}]
df = spark.createDataFrame(data)

#Mostrar el dataframe 
df.show()

#Leer archivos desde S3 