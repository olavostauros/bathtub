from bathtub import handlers
from firenado import tornadoweb


class BathtubComponent(tornadoweb.TornadoComponent):

    def get_handlers(self):
        return [
            (r'/', handlers.IndexHandler),
        ]
