from aficionado import Aficionado

from .tools import call_app

app = Aficionado()

def test_app ():
  @app.route('/')
  def index():
    return 'Hello World'

  @app.route('/page')
  def page():
    return 'Hello World'

def test_route ():
  assert True