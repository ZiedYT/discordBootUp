import discord
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
RELAIS_1_GPIO = 17
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)
GPIO.output(RELAIS_1_GPIO, GPIO.LOW)


client = discord.Client()

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	print( message)
	if message.author == client.user:
		return

	else:
		GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)
		time.sleep(1)	
		GPIO.output(RELAIS_1_GPIO, GPIO.LOW)

client.run("YOUR-DISCORD-BOT-TOKEN-HERE")