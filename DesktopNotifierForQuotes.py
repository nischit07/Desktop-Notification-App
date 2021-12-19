import datetime
import time
import requests
from plyer import notification


quotes= None
try:
    quotes = requests.get("https://zenquotes.io/api/random")
    if (quotes != None):
        data = quotes.json()[0]
        while True:
            notification.notify(
                        title="Quote of the hour".format(datetime.date.today()),
                        message="{quoteofthehour}".format(quoteofthehour=data['q']),
                        app_icon="Food_for_Thought.ico",
                        timeout=30
                    )
            time.sleep(60*60)
except:
    print("Please! Check your internet connection")