from aficionado import Response

def test_response():
    '''
    Test the response object
    '''
    res = Response('Hello World')

    assert res._body == 'Hello World'
    assert res.body == 'Hello World'

def test_response_headers():
    '''
    Test response headers
    '''
    res = Response('Hello World')

    assert type(res.headers).__name__ == 'MultiDictMap'

def test_response_body():
    '''
    Test response body
    '''
    res = Response('Hello World')

    assert res._body == 'Hello World'
    assert res.body == 'Hello World'