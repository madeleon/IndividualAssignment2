import os
from wsgiref.simple_server import make_server # the wsgiref webserver (default with Python)
from pyramid.config import Configurator

from pyramid.response import FileResponse
from pyramid.renderers import render_to_response

def basic_route(req):
    return FileResponse('homepage.html')

def Analysis(req): 
  return FileResponse('analysis.html')


def main() :
  with Configurator() as config:

    # basic_route
    config.add_route('homepage', '/')  #every route you add, you have to add a view
    config.add_view(basic_route, route_name='homepage')

    # for all templates
    config.include('pyramid_jinja2')
    config.add_jinja2_renderer('.html')

    config.add_route('Analysis', '/Analysis')
    config.add_view(Analysis, route_name='Analysis')
    
    # add static folder to search path
    config.add_static_view(name='/', path='./public', cache_max_age=3600)

    # create the webserver config
    app = config.make_wsgi_app()

    port = int(os.environ.get("PORT", 5000))
  # run the server
  server = make_server('0.0.0.0', port, app)
  print("The server is now running on: http://127.0.0.1:8080")
  
  try:
    server.serve_forever()
  except KeyboardInterrupt:
    print("\nExiting...")
    exit(0)

if __name__ == '__main__':
  main()
