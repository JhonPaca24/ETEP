import findspark
findspark.init()

import boto3
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit

# Configura SparkSession
spark = SparkSession.builder \
    .appName("PySpark Glue Simulado") \
    .getOrCreate()

# Leer CSV desde S3 (mismo nombre de bucket que en Terraform)
s3_input_path = "s3a://pyspark-demo-bucket-jp/input/usuarios.csv"

# Leer el archivo CSV
df = spark.read.option("header", "true").csv(s3_input_path)

print("✅ Datos originales:")
df.show()

# Transformaciones: filtro y nueva columna
df_filtrado = df.filter(col("edad") > 30)
df_agregado = df_filtrado.withColumn("pais", lit("Colombia"))

print("✅ Datos filtrados:")
df_agregado.show()

# Guardar en S3 en formato Parquet
output_path = "s3a://pyspark-demo-bucket-jp/output/usuarios_filtrados/"
df_agregado.write.mode("overwrite").parquet(output_path)

print("✅ Transformación y escritura completa.")

