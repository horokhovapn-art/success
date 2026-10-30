variable "region" {
  type    = string
  default = "us-east-1"
}
variable "project_name" { type = string }
variable "app_urls" { type = list(string) }
variable "cors_origins" { type = list(string) }
variable "image_uri" { type = string }
variable "parser_role_name" { type = string }
variable "parser_model" {
  type    = string
  default = "us.amazon.nova-lite-v1:0"
}
