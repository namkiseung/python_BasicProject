import requests
url = "http://www.op.gg"
res = requests.get(url)
with open("op_gg.html", "w") as f:
    f.write(res.content)    

'''
[res 사용법]

['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__',
'__doc__', '__enter__', '__exit__', '__format__', '__getattribute__', 
'__getstate__', '__hash__', '__init__', '__iter__', '__module__', '__new__',
 '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
  '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
  '_content', '_content_consumed', '_next', 'apparent_encoding', 'close', 
  'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers',
   'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 
   'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw',
    'reason', 'request', 'status_code', 'text', 'url']

'''
