output "user_pool_id" { value = aws_cognito_user_pool.main.id }
output "user_pool_client_id" { value = aws_cognito_user_pool_client.web.id }
output "issuer" { value = "https://cognito-idp.${var.region}.amazonaws.com/${aws_cognito_user_pool.main.id}" }
output "hosted_domain" { value = "${aws_cognito_user_pool_domain.main.domain}.auth.${var.region}.amazoncognito.com" }
output "google_redirect_uri" { value = "https://${aws_cognito_user_pool_domain.main.domain}.auth.${var.region}.amazoncognito.com/oauth2/idpresponse" }
output "parser_url" { value = aws_lambda_function_url.parser.function_url }
output "parser_function_name" { value = aws_lambda_function.parser.function_name }
