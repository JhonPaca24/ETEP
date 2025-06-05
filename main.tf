provider "aws" {
  region     = "us-east-1"
  access_key = var.aws_access_key_id
  secret_key = var.aws_secret_access_key
}

resource "aws_s3_bucket" "pyspark_demo" {
  bucket        = var.bucket_name
  force_destroy = true
}

resource "aws_s3_object" "usuarios_csv" {
  bucket       = aws_s3_bucket.pyspark_demo.bucket
  key          = "input/usuarios.csv"
  source       = "./usuarios.csv"
  etag         = filemd5("./usuarios.csv")
  content_type = "text/csv"
}