from aficionado.response import Response

class Route:
  def __init__(self, path, handler, allowed_methods):
    '''
    Constructor
    '''
    self.path = path
    self.handler = handler
    self.allowed_methods = allowed_methods

  def handle(self):
    '''
    Handle the request
    '''
    res = self.handler()

    if not isinstance(res, Response):
      return Response(res)

    return res