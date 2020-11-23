class MultiDictMap():
  def __init__(self):
    pass

class Response():
  def __init__(self, body=None):
    self._body = body
    self._headers = MultiDictMap()

  @property
  def headers(self):
    return self._headers

  @property
  def body(self):
    return self._body