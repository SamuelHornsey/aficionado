import pytest

from aficionado import Aficionado, Response
from tests.tools import (
  call_app,
  create_app,
  read_event
)

app = Aficionado()

# <?[a-zA-Z0-9_-]+:[a-zA-Z0-9_-]+>

def test_app():
  '''
  Test the main app
  '''
  @app.route('/')
  def index():
    return 'Hello World'

  @app.route('/page')
  def page():
    return 'Hello World'

  assert '/' in app.router.routes
  assert len(app.router.routes['/']) == 1

def test_static_route():
  '''
  Test route decorator
  '''
  def handler():
    return 'Hello World'

  app.route('/page_2')(handler)

  assert '/' in app.router.routes
  assert len(app.router.routes['/']) == 1

def test_handler(create_app):
  '''
  Test handler function
  '''
  res = call_app(app)
  assert res.body == 'Hello World'

  res = create_app(read_event('default'), {})
  assert res.body == 'Hello World'

  response = Response('Hello World')

  @create_app.route('/')
  def index():
    return response

  res = call_app(create_app)
  assert res == response