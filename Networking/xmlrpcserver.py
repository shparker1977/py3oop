import xmlrpc.server

class XMLRPCServices:

    class ExposedServices:
        pass

    def __init__(self, **services):
        self.services = self.ExposedServices()
        for name, service in services.items():
            setattr(self.services, name, service)

    def serve(self, host='localhost', port=7777):
        print('Serving XML-RPC on {}:{}'.format(host, port))
        self.server = xmlrpc.server.SimpleXMLRPCServer((host,port))
        self.server.register_introspection_functions()
        self.server.register_instance(self.services, allow_dotted_names=True)
        self.server.serve_forever()

    def stop(self):
        self.server.shutdown()
        self.server.server_close()


class MathServices:
    def double(self, v):
        return v**2

class TimeServices:
    def currentTime(self):
        import datetime
        return datetime.datetime.utcnow()

if __name__ == "__main__":
    xmlrpcserver = XMLRPCServices(math=MathServices(), time=TimeServices())
    import threading
    server_thread = threading.Thread(target=xmlrpcserver.serve)
    server_thread.start()

    from xmlrpc.client import ServerProxy
    client = ServerProxy("http://localhost:7777")
    print(client.time.currentTime())
    print(client.math.double(7))
    xmlrpcserver.stop()
    server_thread.join()