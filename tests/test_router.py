import pytest

from aficionado.router import Router
from aficionado.route import Route

from tests.tools import create_app

@pytest.fixture
def create_router():
  '''
  Creates a router for testing
  '''
  router = Router()

  def handler():
    return 'hello world'

  router.add(Route(
    path='/',
    handler=handler,
    allowed_methods=['GET', 'POST']
  ))

  return router

def test_router_add(create_router):
  '''
  Tests the router add
  '''
  assert '/' in create_router.routes

  with pytest.raises(Exception) as ex:
    create_router.add(Route(
      path='/',
      handler=lambda: None,
      allowed_methods=['FAKE_METHOD']
    ))

  assert str(ex.value) == 'HTTP method FAKE_METHOD is not valid'

def test_router_find_route(create_router):
  '''
  Tests finding a route on the router
  '''
  route = create_router.find_route('/', 'GET')
  assert isinstance(route, Route)

  with pytest.raises(Exception) as ex:
    route = create_router.find_route('/bad_route', 'GET')

  assert str(ex.value) == 'Method GET cannot be found on path /bad_route'