from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 4321

#creating Handler class to handle the http request
class Handler(BaseHTTPRequestHandler):

    print("The Server is running and serving at port" ,PORT)
    #function to handle get request
    def do_GET(this):
        
        if this.path == '/':
            this.path = '/home.html'
        try:
            #open the html file then get its content
            file = open(this.path[1:]).read()
            this.send_response(200)
        except:
            file = "404 Not Found"
            this.send_response(404)
        #end headers beacause we used send_response()    
        this.end_headers()
        
        #writing file content on the screen
        this.wfile.write(file.encode('utf-8'))
        
#creating the server object and passing port no and the handler class to it
server = HTTPServer(('', PORT), Handler)
server.serve_forever()