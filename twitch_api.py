from twitch import TwitchClient
import requests
client = TwitchClient(client_id='nucabes1ry0ctw3ilp2d2u1uxkgmef')

#Convert UserName to User_ID ["esl_csgo","temp"] ==> 123456, 112211
user_name = "esl_csgo"
USER = client.users.translate_usernames_to_ids('esl_csgo')
user_id= USER[0]['id']
print(user_id)

response = client.streams.get_stream_by_user(user_id)
print(response)

live_user_url = f"http://tmi.twitch.tv/group/user/{user_name}/chatters"
live_url_response = requests.get(live_user_url)
temp=live_url_response.json()['chatters']['viewers']

print(temp)
