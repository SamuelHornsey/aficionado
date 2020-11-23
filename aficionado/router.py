import re

from aficionado.route import Route

class PathNotFoundException(Exception):
  pass

class MethodDoesNotExistException(Exception):
  pass

class MethodNotAllowedException(Exception):
  pass

HTTP_METHODS = [
  'GET',
  'POST',
  'UPDATE',
  'DELETE',
  'HEAD'
]

class Router:
  def __init__(self):
    '''
    Constructor
    '''
    self.routes = {}

  def add(self, route):
    '''
    Add a route to the router

    Parameters:
      self (Router): self object
      route (Route): route object
    '''
    for method in route.allowed_methods:
      if method not in HTTP_METHODS:
        raise MethodDoesNotExistException(f'HTTP method {method} is not valid')
      
      self.routes.setdefault(route.path, {})
      self.routes[route.path][method] = route

  def find_route(self, path, method='GET'):
    '''
    Find the current route

    Parameters:
      self (Router): self object
      path (str): search path 

    Returns:
      route (Route): found route object
    '''
    try:
      return self.routes[path][method]
    except KeyError:
      if not self.routes.get(path):
        raise PathNotFoundException(
          f'Resource {path} could not be found')
      if not self.routes[path].get(method):
        raise MethodNotAllowedException(
          f'Method {method} not allowed on resource {path}')
    

