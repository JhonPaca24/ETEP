variable "region"{
  default = "us-east-1"
}

variable "aws_access_key_id" {
  description = "AWS Access Key ID"
  type        = string
  sensitive   = true
}

variable "aws_secret_access_key" {
  description = "AWS Secret Access Key"
  type        = string
  sensitive   = true
}
variable "bucket_name" {
  description = "pyspark-demo-bucket-jp"
  type        = string
}

