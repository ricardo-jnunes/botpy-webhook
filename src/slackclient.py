import slack

slack_token = 'xoxb-500777235730-657970759639-xsvyRdPkX3vL3J3AWrWtNCv2'#os.environ["SLACK_API_TOKEN"]
rtmclient = slack.RTMClient(token=slack_token)

@slack.RTMClient.run_on(event='message')
def say_hello(**payload):
    data = payload['data']
    if 'Hello' in data['text']:
        channel_id = data['channel']
        thread_ts = data['ts']
        user = data['user']

        webclient = payload['web_client']
        webclient.chat_postMessage(
            channel=channel_id,
            text="Hi <@{}>!".format(user),
            thread_ts=thread_ts
        )

rtmclient.start()