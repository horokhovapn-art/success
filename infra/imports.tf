import {
  to = aws_cognito_user_pool.main
  id = "us-east-1_HjS5pstAU"
}
import {
  to = aws_cognito_user_pool_domain.main
  id = "successfulsuccess-127555670831"
}
import {
  to = aws_cognito_identity_provider.google
  id = "us-east-1_HjS5pstAU:Google"
}
import {
  to = aws_cognito_user_pool_client.web
  id = "us-east-1_HjS5pstAU/i0469fut0hqk1vdt430ii1u9s"
}
import {
  to = aws_iam_role.parser
  id = "successfulsuccess-ai-ParserRole-SF81aodFC1xI"
}
import {
  to = aws_iam_role_policy_attachment.parser_basic
  id = "successfulsuccess-ai-ParserRole-SF81aodFC1xI/arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}
import {
  to = aws_iam_role_policy.bedrock
  id = "successfulsuccess-ai-ParserRole-SF81aodFC1xI:bedrock-invoke"
}
import {
  to = aws_cloudwatch_log_group.parser
  id = "/aws/lambda/successfulsuccess-agenda-parser"
}
import {
  to = aws_lambda_function.parser
  id = "successfulsuccess-agenda-parser"
}
import {
  to = aws_lambda_function_url.parser
  id = "successfulsuccess-agenda-parser"
}
