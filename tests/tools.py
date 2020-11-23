''' Testing Tools '''
import pytest
import json

from aficionado import Aficionado
from pathlib import Path
from aws_lambda_context import LambdaContext

def read_event(event):
  path = Path(__file__).parent
  return json.loads(open(f'{path}/events/{event}.json', 'r').read())

def call_app(app, event='default'):
  lambda_context = LambdaContext()
  event = read_event(event)
  return app.handler(event, lambda_context)

@pytest.fixture(autouse=True)
def create_app():
  app = Aficionado()

  @app.route('/')
  def index():
    return 'Hello World'

  yield app