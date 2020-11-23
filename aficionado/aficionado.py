from aficionado.route import Route
from aficionado.router import Router
from aficionado.request import request

class Aficionado:
  '''
  Aficionado application object. This application 
  is initialised to create the handlers
  '''

  def __init__(self):
    '''
    Constructor
    '''
    self.router = Router()

  def add_route(self, handler, path, methods):
    '''
    Add a route handler to the application

    Parameters:
      self (Aficionado): self object
      handler (function): route handler function
      path (str): route path
      methods (list): allowed methods for route
    '''
    route = Route(
      path=path,
      handler=handler,
      allowed_methods=methods
    )

    self.router.add(route)

  def route(self, path, methods=['GET']):
    '''
    Route decorator

    Parameters:
      self (Aficionado): self object
      path (str): the handler path
      methods (list): the allowed handler methods

    Returns:
      decorator (function): a handler function
    '''
    def decorator(function):
      self.add_route(function, path, methods)
      return function

    return decorator

  def __call__(self, *args, **kwargs):
    '''
    Proxy to handler func
    '''
    return self.handler(*args, **kwargs)

  def handler(self, event, context):
    '''
    The lambda handler

    Parameters:
      self (Aficionado): self object
      event (dict): event object
      context (Context): AWS lambda context

    Returns:
      response (dict): response dictionary
    '''
    request.build_request(event, context)
    return self.router.find_route(request.path, request.method).handle()

