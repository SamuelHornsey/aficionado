# imports
from aficionado.route import Route
from aficionado.defaults import not_found_handler, internal_error_handler

class Router:
  def __init__(self):
    '''
    Constructor
    '''

    # create route for not found
    not_found = Route(
      path=None,
      handler=not_found_handler,
      allowed_methods=['ALL']
    )

    self.routes = []
    self.not_found_route = not_found

  def add (self, route):
    '''
    Add a route to the router

    Parameters:
      self (Router): self object
      route (Route): route object
    '''

    # check that route is not already in routes
    for r in self.routes:
      if r.path == route.path:
        raise Exception('Path {path} already exists'.format(route.path))

    self.routes.append(route)

  def find_route (self, path):
    '''
    Find the current route

    Parameters:
      self (Router): self object
      path (str): search path 

    Returns:
      route (Route): found route object
    '''

    # find route in list
    for r in self.routes:
      if r.path == path:
        return r

    return self.not_found_route

  def not_found(self, handler):
    '''
    Set the not found handler

    Parameters:
      self (Router): self object
      handler (function): handler function
    '''
    not_found = Route(
      path=None,
      handler=handler,
      allowed_methods=['ALL']
    )

    self.not_found_route = not_found

    

