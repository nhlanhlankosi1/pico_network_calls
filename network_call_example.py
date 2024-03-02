# A simple example that:
# - Connects to a WiFi Network defined by "ssid" and "password"
# - Performs a GET request (loads a webpage)
# - Queries the current time from a server

import network   # handles connecting to WiFi
import urequests # handles making and servicing network requests
import time

# Connect to network
wifi = network.WLAN(network.STA_IF)
wifi.active(True)

# Fill in your network name (ssid) and password here:
ssid = 'iPhone X'
password = 'MakerCulture7!'
wifi.connect(ssid, password)

# wait for the raspberry pi to be connected to the internet  
while wifi.isconnected() == False:
    print('Waiting for Connection . . .')
    time.sleep(1)

# get the ip address of the raspberry
wifiInfo = wifi.ifconfig()
IP_address = wifiInfo[0]
print(IP_address)

# make HTTP requests
# Example 1. Make a GET request for google.com and print HTML
# Print the html content from google.com
print("1. Querying google.com:")
r = urequests.get("http://www.google.com")
print(r.content)
r.close()

# Example 2. urequests can also handle basic json support! Let's get the current time from a server
print("\n\n2. Querying the current GMT+0 time:")
r = urequests.get("http://date.jsontest.com") # Server that returns the current GMT+0 time.
print(r.json())



