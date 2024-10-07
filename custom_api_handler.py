from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class CustomAPIHandler(BaseHTTPRequestHandler):
    def do_PUT(self):
        """ 
        Extract the Content-Length so that, 
        we know how much data we have to parse 
        """
        content_length = int(self.headers.get('Content-Length'))
        request_body = self.rfile.read(content_length).decode('utf-8')

        try:
            data = json.loads(request_body)
            name = data.get('name')
            email = data.get('email')
            tag = data.get('tag')
            
            response_data = {
                'status': 'success',
                'message': f'User {name} with email {email} has been added with tag {tag}.'
            }
            """ Send an HTTP status code of 200 (OK) """
            self.send_response(200) 

        except json.JSONDecodeError:
            response_data = {
                'status': 'error',
                'message': 'Invalid JSON input.'
            }
            """ Send an HTTP status code of 400 (Bad Request) """
            self.send_response(400)
        
        """ Inform the client we are sending JSON """ 
        self.send_header('Content-type','application/json') 

        """ Finish sending headers """
        self.end_headers()

        """ Send the JSON response body """
        self.wfile.write(json.dumps(response_data).encode('utf-8'))


def run(server_class=HTTPServer,handler_class=CustomAPIHandler,port=5555):
    server_address = ('',port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()

