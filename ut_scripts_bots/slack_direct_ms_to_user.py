from slackclient import SlackClient

SLACK_TOKEN = "xoxb-bottoken" # or a TEST token. Get one from https://api.slack.com/docs/oauth-test-tokens

slack_client = SlackClient(SLACK_TOKEN)
api_call = slack_client.api_call("im.list")

# You should either know the user_slack_id to send a direct msg to the user
user_slack_id = "USLACKBOT"

if api_call.get('ok'):
    for im in api_call.get("ims"):
        if im.get("user") == user_slack_id:
            im_channel = im.get("id")
            slack_client.api_call("chat.postMessage", channel=im_channel,
                                       text="Hi Buddy", as_user=True)
