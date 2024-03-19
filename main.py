import logging
from wsgiref.simple_server import make_server

from spyne.application import Application
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

from CORSMiddleware import CORSMiddleware
from roadService import RoadService

application = Application([RoadService], 'soap-volte.mathis-mazoyer.fr',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11()
                          )

HOST = "0.0.0.0"
PORT = 3051


def main():
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)
    logging.info(f'listening on {HOST}:{PORT}')
    logging.info(f'wsdl is at: http://{HOST}:{PORT}/?wsdl')

    wsgi_application = WsgiApplication(application)
    app_with_cors = CORSMiddleware(wsgi_application)

    server = make_server(HOST, PORT, app_with_cors)
    server.serve_forever()


if __name__ == '__main__':
    print("ok")
    main()
