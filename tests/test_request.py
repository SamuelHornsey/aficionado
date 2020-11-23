from aficionado import request
from tests.tools import call_app, create_app

def test_request_path(create_app):
  '''
  Test the request object path
  '''
  res = call_app(create_app)

  assert request.path == '/'

def test_request_method(create_app):
  '''
  Test the request method
  '''
  res = call_app(create_app)

  assert request.method == 'GET'

def test_request_headers(create_app):
  '''
  Test the request headers
  '''
  res = call_app(create_app)

  assert 'some-header' in request.headers
  assert request.headers.get('non-header') == None
  assert request.headers.get('some-header') == 'a-header'

def test_request_query_params(create_app):
  '''
  Test the request query params
  '''
  res = call_app(create_app)
  print(res)
