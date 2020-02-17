import http.server
import json
import os
import threading

from Selenium import Browser

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        ctype = self.headers['content-type']
        if ctype == "application/json":
            content_lenght = int(self.headers['Content-Length'])
            global data
            data = json.loads(self.rfile.read(content_lenght).decode())
            self.send_response_only(200)
            self.end_headers()
            if data["info"]["browser"] == "yes" and not driver.isBrowserOpen:
                driver.open_browser()
            action[data["action"]]()
        else:
            self.send_error(404)
        return


driver = Browser()
action = {
    "poweroff": lambda: os.system("poweroff"),
    "netflix_search": lambda: driver.netflix_search(data["info"]["movie"]),
    "primevideo_search": lambda: driver.primevideo_search(data["info"]["movie"]),
    "yt_search": lambda: driver.yt_search(data["info"]["video"]),
    "close_browser": driver.close_browser
}
