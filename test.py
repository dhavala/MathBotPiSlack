from slackclient import SlackClient
import time
import os

slack_client = SlackClient(os.environ.get('SLACK_MATHBOT_TOKEN'))

api_call = slack_client.api_call("users.list")
if api_call.get('ok'):
	users = api_call.get('members')
	for user in users:
		print(user.get('name'))



if slack_client.rtm_connect(with_team_state=False):
	print("Successfully connected, listening for events")
	while True:
		print(slack_client.rtm_read())
		
		time.sleep(1)
else:
	print("Connection Failed")