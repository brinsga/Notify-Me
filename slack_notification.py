from topbooks import *
#getting webhook url from config file
webhooks_url = config['slack']['url']

#book data to be sent
data = {
    "blocks": [
    {
            "type": "section",
            "text": {
                "type": "plain_text",
                "text": "There is a new trending book"
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "fields": [{
                    "type": "plain_text",
                    "text": str(top15books[1])
                },
                {
                    "type": "plain_text",
                    "text": str(top15author[1])
                }
            ]
        }
    ]
}
print(data)

def sendSlackNotification():
    """
        Sends a notification of a recent bestseller to a slack channel.
    
    """
    post_response = requests.post(webhooks_url, data=json.dumps(data),
        headers={'Content-Type': 'application/json'})
    if(post_response.status_code != 200):
        print("Post message request to slack returned an error. \n Response: "
            + str(post_response.status_code) + "  " + str(post_response.text))
    else:
        print("Slack Notification Sent")

#Send a slack notification about a new trending book
sendSlackNotification()







