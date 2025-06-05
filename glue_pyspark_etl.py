import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit

# Crear sesión de Spark
spark = SparkSession.builder \
    .appName("PySpark S3 Demo") \
    .getOrCreate()

# Leer CSV desde S3
s3_input_path = "s3://pyspark-demo-bucket-jp/input/usuarios.csv"
df = spark.read.option("header", "true").csv(s3_input_path)

print("✅ Datos originales:")
df.show()

# Filtrar por edad > 30 y agregar columna 'pais'
# Convertimos edad a int en caso de que venga como string
df = df.withColumn("edad", col("edad").cast("int"))
filtrados = df.filter(col("edad") > 30)
agregado = filtrados.withColumn("pais", lit("Colombia"))

print("✅ Datos filtrados y transformados:")
agregado.show()

# Guardar resultado en S3 como Parquet
output_path = "s3://pyspark-demo-bucket-jp/output/usuarios_filtrados/"
agregado.write.mode("overwrite").parquet(output_path)

print("✅ Transformación y escritura completadas.")
