# import libraries
from selenium import webdriver
from time import sleep


class VideoWatcher:
    """
    Watches youtube videos
    """
    # define a class variable to track total watches
    total_watches = 0

    def __init__(self, driver_path: str, link: str):
        """ Makes a video watching object

        :param driver_path: The current driver path that is being used
        :param link: The link that is to be accessed
        """
        self.link = link
        # create 5 of the same drivers to watch the video 5 times
        self.drivers = [webdriver.Chrome(executable_path=driver_path) for i in range(8)]

    def watch_video(self) -> None:
        """ Watches a youtube video

        :return: nothing
        """
        # loop through drivers and open a video
        for driver in self.drivers:
            driver.get(self.link)
            VideoWatcher.total_watches += 1
            print("Watch #", VideoWatcher.total_watches)
        # pause for 31 seconds after this
        sleep(31)


# set path variables
driver_path = "C:/Users/14165/Dev/drivers/chromedriver.exe"
yt_link = "https://www.youtube.com/watch?v=pHK2jb77Fi8&t=8s"
watches = 80

# create a watching object
yt_watcher = VideoWatcher(driver_path, yt_link)

# call the method to watch videos
while yt_watcher.total_watches < watches:
    yt_watcher.watch_video()

# closer all drivers
for driver in yt_watcher.drivers:
    driver.close()
