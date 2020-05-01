#!/usr/bin/env python3

import requests
import json
import time
from settings import *

# set nextcloud header
headers = {'OCS-APIRequest': 'true',
           'Content-Type': 'application/json',
           'Accept': 'application/json'
          }

# set gotify header
headerspush = {'X-Gotify-Key': token}

# create empty messages list
notifications = []

# start infinite loop for listening
if __name__ == "__main__":
    while True:
        # retrieve json data from the notifications endpoint
        r = requests.get(url, headers=headers, auth=(user, pw))
        # load the json data
        m = (r.json())
        # Iterate through the notifications
        for i in range(len(m["ocs"]["data"])):
            notification_id = m["ocs"]["data"][i]["notification_id"] # id
            title = m["ocs"]["data"][i]["subject"]
            date  = m["ocs"]["data"][i]["datetime"]
            msg   = m["ocs"]["data"][i]["message"] or " "
            # check if message was already pushed
            if notification_id in notifications:
                continue
            # else send push notification
            else:
                requests.post(
                    urlpush, 
                    headers=headerspush, 
                    data={
                        'id': notification_id, 
                        'date': date,
                        'title': title, 
                        'message': msg, 
                        'priority': notification_priority,
                        'extras': {
                            'client::display': {
                                'contentType': 'text/markdown'
                            }
                        }})
                # Add the message to the list
                notifications.append(notification_id)
        # wait before checking again
        time.sleep( delay )
