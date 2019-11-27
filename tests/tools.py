''' Testing Tools '''
from aws_lambda_context import LambdaContext

def call_app(app):
  lambda_context = LambdaContext()
  return app.handler({}, lambda_context)