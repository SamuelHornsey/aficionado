# imports
from aficionado.route import Route
from aficionado.router import Router

class Aficionado:
  '''
  Aficionado application object. This application is initialised
  to create the handlers
  '''

  def __init__(self):
    self.router = Router()

  def add_route (self, handler, path, methods):
    '''
    Add a route handler to the application

    Parameters:
      self (Aficionado): self object
      handler (function): route handler function
      path (str): route path
      methods (list): allowed methods for route

    Returns:
      None
    '''
    route = Route(
      path=path,
      handler=handler,
      allowed_methods=methods
    )

    self.router.add(route)

  def route (self, path, methods=['GET']):
    '''
    Route decorator

    Parameters:
      self (Aficionado): self object
      path (str): the handler path
      methods (list): the allowed handler methods

    Returns:
      decorator (function): a handler function
    '''
    def decorator (function):
      self.add_route(function, path, methods)
      return function

    return decorator

  def not_found(self):
    def decorator(function):
      self.router.not_found(function)
      return function

    return decorator

  def handler (self, event, context):
    pass

