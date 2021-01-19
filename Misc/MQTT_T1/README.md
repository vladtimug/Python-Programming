<h1>The project uses the python module 'paho' to implement a mqtt client which interracts with a RaspberryPi read/write built-in capabilities.</h1>

The client responds to the following messages:
  + 'on_green' - turns on the built-in green LED from the Pi
  + 'off_green' - turns off the built-in green LED from the Pi
  + 'on_red' - turns on the built-in red LED from the Pi
  + 'off_red' - turns off the built-in red LED from the Pi
  + 'host_temp' - displays the value read by the built-in temperature sensor on the Pi for both GPU and CPU, toghether with the date, time and hostname
  + 'host_voltage' - displays the value read by the built-in voltage sensor on the Pi, toghether with the date, time and hostname
  + 'host_freq' - displays the frequency of the Pi core in MHz, toghether with the date, time and hostname
  + 'heartbeat_green' - engages the green LED in a heartbeat behaviour
  + 'heartbeat_green_off' - disengages the green LED from the heartbeat behaviour
  + 'heartbeat_red' - engages the red LED in a heartbeat behaviour
  + 'heartbeat_red_off' - disengages the red LED from the heartbeat behaviour

Default topic is TOPIC_1. It is recommended to change it to a relevant name.

The publisher of the message can be either a mosquitto instance from the terminal for demonstration purposes or a dashboard panel from IoT MQTT Panel application found on Play Store. Make sure to use the same IP adress when configuring the mosquitto publisher or the panel dashbord from the android app. For more info on syntax for mosquitto publisher, do 'sudo apt update && sudo apt -y upgrade && sudo apt install mosquitto' in your terminal. 

Run script with sudo permissions.
