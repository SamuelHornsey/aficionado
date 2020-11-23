class Request():
  def build_request(self, event, context):
    '''
    Build the request object from
    event and context

    Parameters:
      self (Request): self object
      event (Dict): event dictionary
      context (LambdaContext): lambda context
    '''
    # TODO place vars in dict containers
    self._query_params = event['multiValueQueryStringParameters']
    self._headers = event['headers']

    self.method = event['requestContext']['httpMethod']
    self.path = event['requestContext']['resourcePath']

  @property
  def headers(self):
    '''
    Get the request headers
    '''
    return self._headers

  @property
  def query_params(self):
    '''
    Get the request query params
    '''
    return self._query_params

request = Request()