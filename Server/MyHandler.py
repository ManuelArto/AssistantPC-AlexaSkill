import http.server
import json
import os
import threading

from helpers.BrowserDriver import Browser

class MyHandler(http.server.BaseHTTPRequestHandler):
	def __init__(self, request, client_address, server):
		self.driver = Browser()
		self.action = {
			"poweroff": lambda: print("poweroff"), #os.system("poweroff"),
			"netflix_search": lambda: self.driver.netflix_search(self.data["info"]["movie"]),
			"primevideo_search": lambda: self.driver.primevideo_search(self.data["info"]["movie"]),
			"yt_search": lambda: self.driver.yt_search(self.data["info"]["video"]),
			"close_browser": self.driver.close_browser
		}
		http.server.BaseHTTPRequestHandler.__init__(self, request, client_address, server)

	def do_POST(self):
		ctype = self.headers['content-type']
		if ctype == "application/json":
			content_lenght = int(self.headers['Content-Length'])
			self.data = json.loads(self.rfile.read(content_lenght).decode())
			self.send_response_only(200)
			self.end_headers()
			if self.data["info"]["browser"] == "yes" and not self.driver.isBrowserOpen:
				self.driver.open_browser()
			thread = threading.Thread(target=self.action[self.data["action"]])
			thread.start()
		else:
			self.send_error(404)
		return


