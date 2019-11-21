import logging
import slack
from bot import bot

slack_token = 'xoxb-2968906276-830432063666-XXXXXXXXXXXXXXXXXXXX'#os.environ["SLACK_API_TOKEN"]
rtmclient = slack.RTMClient(token=slack_token)

@slack.RTMClient.run_on(event='message')
def say_hello(**payload):
    data = payload['data']
    print(data)
    if any(x in data['text'].split() for x in ['<@UQECQ1VKL>']):
        text = data['text'].replace('<@UQECQ1VKL>', '')
        channel_id = data['channel']
        #thread_ts = data['ts']
        #user = data['user']

        webclient = payload['web_client']
        webclient.chat_postMessage(
            channel=channel_id,
            text="{}".format(bot.speak(text))
            #thread_ts=thread_ts
        )
    

logging.info('Starting BotPy')
print("Starting")
rtmclient.start()