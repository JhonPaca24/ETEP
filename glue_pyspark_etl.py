import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import col, lit

# 🔹 Obtener argumentos del job (necesario para Glue)
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

# 🔹 Crear contexto de Spark y Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# 🔹 Inicializar job
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# 🔹 Leer datos desde Glue Catalog
dyf_usuarios = glueContext.create_dynamic_frame.from_catalog(
    database="data_spark_user_jp",
    table_name="input"  # Reemplaza si el nombre real es diferente
)

# 🔹 Convertir a DataFrame para procesar con PySpark
df = dyf_usuarios.toDF()

# 🔹 Filtrar por edad > 30 y agregar columna 'pais'
filtrados = df.filter(col("edad") > 30)
agregado = filtrados.withColumn("pais", lit("Colombia"))

print("Datos filtrados:")
agregado.show()

# 🔹 Convertir a DynamicFrame
dyf = DynamicFrame.fromDF(agregado, glueContext, "dyf")

# 🔹 Guardar resultado en S3 como Parquet
output_path = "s3://pyspark-demo-bucket-jp/output/usuarios_filtrados/"
glueContext.write_dynamic_frame.from_options(
    frame=dyf,
    connection_type="s3",
    connection_options={"path": "s3://target-pyspark-demo-bucket-jp"},
    format="parquet"
)

# 🔹 Finalizar job
job.commit()

print("✅ Transformación completa.")