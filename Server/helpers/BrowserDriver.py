from pathlib import Path
from selenium import webdriver

try: 
	from .driver import scripts
	from .credentials import NETFLIX_USERNAME, NETFLIX_PASSWORD
except:
	from driver import scripts
	from credentials import NETFLIX_PASSWORD, NETFLIX_USERNAME


driver_path = "./helpers/driver/chromedriver"
brave_path = "/usr/lib/brave/brave"
user_data_dir = Path("./helpers/driver/User Data")

class Browser:
    def __init__(self):
        self.isBrowserOpen = False

    def close_browser(self):
        self.driver.quit()

    def open_browser(self):
        options = webdriver.ChromeOptions()
        options.binary_location = brave_path
        options.add_argument("--user-data-dir={}".format(user_data_dir))
        options.add_argument('--profile-directory=Default')
        # option.add_argument("--incognito") OPTIONAL
        # option.add_argument("--headless") OPTIONAL
        self.driver = webdriver.Chrome(executable_path=driver_path, options=options)
        self.driver.maximize_window()
        self.isBrowserOpen = True

    def netflix_search(self, movie):
        print(f"looking for {movie} on netflix")
        scripts.netflix_search(self.driver, movie, NETFLIX_USERNAME, NETFLIX_PASSWORD)

    def primevideo_search(self, movie):
        print(f"looking for {movie} on primevideo")
        scripts.primevideo_search(self.driver, movie)

    def yt_search(self, video):
        print(f"looking for {video} on youtube")
        scripts.youtube_search(self.driver, video)

# Testing
if __name__ == '__main__':
    driver = Browser()
    driver.open_browser()
    driver.netflix_search("the interview")
