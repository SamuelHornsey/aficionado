from aficionado import Aficionado

from .tools import call_app

# init app
app = Aficionado()

def test_app ():
  '''
  Test the main app
  '''
  @app.route('/')
  def index():
    return 'Hello World'

  @app.route('/page')
  def page():
    return 'Hello World'

  assert len(app.router.routes) == 2

def test_route ():
  '''
  Test route decorator
  '''
  def handler ():
    return 'Hello World'

  app.route('/page_2')(handler)

  assert len(app.router.routes) == 3

def test_not_found ():
  '''
  Test not found decorator
  '''
  @app.not_found()
  def not_found ():
    return 'Page not found'

  assert app.router.not_found_route.handler == not_found

def test_handler ():
  '''
  Test handler function
  '''
  res = app.handler({}, {})

  assert res == {}
