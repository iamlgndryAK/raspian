import RPi.GPIO as GPIO
import time
import paho.mqtt.publish as publish

GPIO.setmode(GPIO.BOARD)
trigger_pin = 8
echo_pin = 12

GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)


mqtt_broker_ip = "172.20.10.2"
mqtt_topic = "ultrasonic"


def get_distance():
    GPIO.output(trigger_pin, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(trigger_pin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trigger_pin, GPIO.LOW)

    while GPIO.input(echo_pin) == 0:
        pulse_start_time = time.time()
    while GPIO.input(echo_pin) == 1:
        pulse_end_time = time.time()

    pulse_duration = pulse_end_time - pulse_start_time
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    return distance

try:
    while True:
        distance_cm = get_distance()
        print(f"Distance: {distance_cm} cm")

        mqtt_payload = f"{distance_cm}"
        publish.single(mqtt_topic, payload=mqtt_payload, hostname=mqtt_broker_ip)

        time.sleep(0.05)

except KeyboardInterrupt:
    print("Measurement stopped by user")
    GPIO.cleanup()
