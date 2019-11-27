''' Route object '''

class Route:
  def __init__(self, path, handler, allowed_methods):
    self.path = path
    self.handler = handler
    self.allowed_methods = allowed_methods