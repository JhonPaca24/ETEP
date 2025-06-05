provider "aws" {
  region     = var.region
  access_key = var.aws_access_key_id
  secret_key = var.aws_secret_access_key
}

resource "aws_s3_bucket" "pyspark_demo" {
  bucket        = var.bucket_name
  force_destroy = true
}

resource "aws_s3_bucket" "pyspark_demo_target" {
  bucket        = var.bucket_name_target
  force_destroy = true
}


resource "aws_s3_object" "usuarios_csv" {
  bucket       = aws_s3_bucket.pyspark_demo.bucket
  key          = "input/usuarios.csv"
  source       = "./usuarios.csv"
  etag         = filemd5("./usuarios.csv")
  content_type = "text/csv"
}

resource "aws_s3_object" "registros_colombia_csv"{
  bucket       = aws_s3_bucket.pyspark_demo.bucket
  key          = "input/registro_colombia_1000.csv"
  source       = "./registro_colombia_1000.csv"
  etag         = filemd5("./registro_colombia_1000.csv")
  content_type = "text/csv"
}