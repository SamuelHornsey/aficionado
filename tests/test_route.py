from aficionado.route import Route

def test_route ():
  '''
  Test route object
  '''
  def handler ():
    return 'Hello World'

  route = Route(
    path='/',
    handler=handler,
    allowed_methods=['ALL']
  )

  assert route.handler == handler
  assert route.path == '/'