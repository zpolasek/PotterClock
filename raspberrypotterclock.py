# import Adafruit IO REST client.
from Adafruit_IO import Client, Feed, RequestError

# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = '1d08516a4736427fb95a8dc1626ac27a'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 'zp13'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Assign a Clock feed, if one exists already
try:
    ClockStatusZach = aio.feeds('ClockStatusZach')
except RequestError:  # Doesn't exist, create a new feed
    feed = Feed(name="feederror")
    feederror= aio.create_feed(feed)

# Send a string value 'bar' to the feed 'Foo'.
aio.send_data(ClockStatusZach.key, 'ld_ho')

# avoid timeout from adafruit io
time.sleep(1)

