# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from datetime import datetime
import threading

hostName = "localhost"
serverPort = 8005

#https://www.quackit.com/javascript/javascript_refresh_page.cfm

class MyServer(BaseHTTPRequestHandler):
    refresh = 0


    def do_GET(self):
        now = datetime.now()

        current_time = int(round(time.time() * 1000))#now.strftime("%H:%M:%S")
        #print("Current Time =", current_time)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        #self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))


        #Autorefresh over html is also working but only seconds are supported (not miliseconds)
        '''
        self.wfile.write(bytes(
            "<html><meta http-equiv=\"refresh\" content=\"1;url=index.html\"><head><title>https://pythonbasics.org</title></head>",
            "utf-8"))
        '''

        self.wfile.write(bytes(
            "<html><head><title>https://pythonbasics.org</title><script>function timedRefresh(timeoutPeriod) {setTimeout(\"location.reload(true);\",timeoutPeriod);} window.onload = timedRefresh(100); </script> </head>",
            "utf-8"))

        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("<p>%s - %d</p>" % (current_time, self.refresh), "utf-8"))
        self.wfile.write(bytes("<p>%s - %d</p>" % (current_time, self.refresh), "utf-8"))
        self.wfile.write(bytes("<p>%s - %d</p>" % (current_time, self.refresh), "utf-8"))
        self.wfile.write(bytes("<p>%s - %d</p>" % (current_time, self.refresh), "utf-8"))
        self.wfile.write(bytes("<p>%s - %d</p>" % (current_time, self.refresh), "utf-8"))
        self.wfile.write(bytes("<p>%s - %d</p>" % (current_time, self.refresh), "utf-8"))
        self.wfile.write(bytes("<p>%s - %d</p>" % (current_time, self.refresh), "utf-8"))
        self.wfile.write(bytes("<p>%s - %d</p>" % (current_time, self.refresh), "utf-8"))
        self.wfile.write(bytes("<p>%s - %d</p>" % (current_time, self.refresh), "utf-8"))
        self.wfile.write(bytes("<p>%s - %d</p>" % (current_time, self.refresh), "utf-8"))
        self.wfile.write(bytes("<p>%s - %d</p>" % (current_time, self.refresh), "utf-8"))
        self.wfile.write(bytes("<p>%s - %d</p>" % (current_time, self.refresh), "utf-8"))
        self.wfile.write(bytes("<p>%s - %d</p>" % (current_time, self.refresh), "utf-8"))
        self.wfile.write(bytes("<p>%s - %d</p>" % (current_time, self.refresh), "utf-8"))
        self.wfile.write(bytes("<p>%s - %d</p>" % (current_time, self.refresh), "utf-8"))
        self.wfile.write(bytes("<p>%s - %d</p>" % (current_time, self.refresh), "utf-8"))
        self.wfile.write(bytes("<p>%s - %d</p>" % (current_time, self.refresh), "utf-8"))
        self.wfile.write(bytes("<p>%s - %d</p>" % (current_time, self.refresh), "utf-8"))
        self.wfile.write(bytes("<p>%s - %d</p>" % (current_time, self.refresh), "utf-8"))
        self.wfile.write(bytes("<p>%s - %d</p>" % (current_time, self.refresh), "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
        self.refresh += 1


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
