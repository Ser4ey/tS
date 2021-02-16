from time import sleep

from telethon import TelegramClient
import configparser
config = configparser.ConfigParser()
config.read("config.ini", encoding="utf-8")

api_id = int(config['Resender']['api_id'])
api_hash = config['Resender']['api_hash']
my_channel = config['Resender']['channel_to_send']
client = TelegramClient('resender', api_id, api_hash)
message = config['Resender']['message']

client.start()



async def main():
    while True:
        await client.send_message(my_channel, message)
		print('message sended:', str(message))

with client:
    client.loop.run_until_complete(main())