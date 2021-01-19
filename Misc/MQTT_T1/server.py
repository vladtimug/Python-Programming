# Paho mqtt client code
import paho.mqtt.client as mqtt
from gpiozero import LED 
import subprocess

# The callback for when the client receives a CONNACK response from the server
def on_connect(client, userdata, rc, properties=None):
	print("Connected with result code "+ str(rc))
	client.subscribe("VLAD") # renew subscription to the topic if the client gets disconnected

def on_message(clien, userdata, message):
	message.payload = message.payload.decode("utf-8")
	print(message.topic+" "+str(message.payload))
	if message.payload == 'on_green':
		subprocess.call('echo 1 >/sys/class/leds/led0/brightness', shell=True)
	if message.payload == 'off_green':
		subprocess.call('echo 0 >/sys/class/leds/led0/brightness', shell=True)
	if message.payload == 'on_red':
		subprocess.call('echo 1 >/sys/class/leds/led1/brightness', shell=True)
	if message.payload == 'off_red':
		subprocess.call('echo 0 >/sys/class/leds/led1/brightness', shell=True)
	if message.payload == 'host_temp':
		subprocess.call('./pi-temp.sh', shell=True)
	if message.payload == 'host_voltage':
		subprocess.call('vcgencmd measure_volts', shell=True)
	if message.payload == 'heartbeat_green':
		subprocess.call('echo heartbeat>/sys/class/leds/led0/trigger', shell=True)
		subprocess.call("printf '\n'", shell=True)
	if message.payload == 'heartbeat_green_off':
		subprocess.call('echo none>/sys/class/leds/led0/trigger', shell=True)
	if message.payload == 'heartbeat_red':
		subprocess.call('echo heartbeat>/sys/class/leds/led1/trigger', shell=True)
	if message.payload == 'heartbeat_red_off':
		subprocess.call('echo none>/sys/class/leds/led1/trigger', shell=True)
	if message.payload == 'host_freq':
		subprocess.call('./pi-freq.sh', shell=True)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.loop_forever()
