from driver.script import scripts
from pathlib import Path
from selenium import webdriver


driver_path = "./driver/chromedriver"
brave_path = "/usr/lib/brave/brave"
user_data_dir = Path("./driver/User Data")

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
        scripts.netflix_search(self.driver, movie)

    def primevideo_search(self, movie):
        print(f"looking for {movie} on primevideo")
        scripts.primevideo_search(self.driver, movie)

    def yt_search(self, video):
        print(f"looking for {video} on youtube")
        scripts.youtube_search(self.driver, video)


if __name__ == '__main__':
    driver = Browser()
    driver.open_browser()
    driver.netflix_search("the interview")
