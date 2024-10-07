"""
We are going to create Custom API Handler in this.
We will use BaseHTTPRequestHandler, HTTPServer from http.server 
and json (since modern APIs use JSON for request and response)


First we create our own CustomClass, and inherit it from BaseHTTPRequestHandler,
now, we override the do_PUT method (or any other method you like)

Then, we read the content length from the incoming request headers. 

WHY DO WE READ THE CONTENT LENGTH FROM THE rfile?

self.rfile.read(content_length)
This line is key to understanding how the server reads the data sent by the client.
self.rfile: This is a file-like object associated with the incoming request. 
It represents the body of the request, and you can use it to read the data
that was sent by the client (e.g., form data, JSON, etc.). 
Think of self.rfile as the input stream of the request body.

Why do we call self.rfile.read()?

When a client sends a PUT request, it often includes a request body, 
which contains the data you want to process (e.g., an email, name, tag in this case).
rfile.read(content_length) reads this body from the incoming request.
The content_length is how much data (in bytes) the server should read 
from the request body. This is determined by looking at the Content-Length 
header that the client sends as part of the HTTP request.

Why do we decode it?

After reading the raw bytes from the rfile, you need to convert (decode) 
them from bytes into a string. In most cases, the request body is UTF-8 encoded, 
which is why we use .decode('utf-8').

EXAMPLE FLOW FOR AN PUT API:

PUT /subscribe HTTP/1.1
Host: localhost:8080
Content-Type: application/json
Content-Length: 56

{
    "email": "test@example.com",
    "name": "John Doe",
    "tag": "newsletter"
}

The server will first check the headers and see the Content-Length: 56 header. 
This means the body of the request (the JSON data) is 56 bytes long.

When you call self.rfile.read(56), it reads exactly those 56 bytes 
from the request body (which corresponds to the JSON data).

After reading it, the content looks like this (raw bytes):
b'{"email": "test@example.com", "name": "John Doe", "tag": "newsletter"}'

Then, .decode('utf-8') converts these bytes into a regular Python string:
'{"email": "test@example.com", "name": "John Doe", "tag": "newsletter"}'



Parsing the JSON Request Body:
data = json.loads(request_body)

json.loads(): This function converts the JSON string into a Python dictionary. For example:

After processing the request, you need to send the response back to the client.


"""