# A simple desktop notifier 

import time
from plyer import notification
def Notify(title, message, app_icon):    
    notification.notify(title=title, message=message, app_icon=app_icon, timeout=5)

while (True):
    Notify("Your title", "Your message", "Your icon file name.ico")
    time.sleep(60*60)    # the above function executes every 1 hour unless stopped manually
    
