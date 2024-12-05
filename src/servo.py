import RPi.GPIO as GPIO
import time

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Define servo pins
servo_pins = [17, 18]

# Set up GPIO pins as output
GPIO.setup(servo_pins[0], GPIO.OUT)
GPIO.setup(servo_pins[1], GPIO.OUT)

# Create PWM instances with 50Hz frequency
servo_17 = GPIO.PWM(servo_pins[0], 50)  # GPIO 17
servo_18 = GPIO.PWM(servo_pins[1], 50)  # GPIO 18

# Start PWM with a duty cycle of 0 (stopped)
servo_17.start(0)
servo_18.start(0)

# Function to set servo angle
def set_servo_angle(servo, angle):
    duty = 2 + (angle / 18)  # Calculate duty cycle for the angle
    servo.ChangeDutyCycle(duty)
    time.sleep(0.5)
    servo.ChangeDutyCycle(0)  # Turn off signal to prevent jitter

try:
    # Set servo angles
    print("Setting GPIO 17 to 90 degrees and GPIO 18 to 0 degrees")
    set_servo_angle(servo_17, 0)  # Turn GPIO 17 servo to 0 degrees
    set_servo_angle(servo_18, 0)   # Turn GPIO 18 servo to 0 degrees
    
    # Keep the servos in place
    time.sleep(2)
    
except KeyboardInterrupt:
    print("Program interrupted")
finally:
    # Clean up GPIO and stop PWM
    servo_17.stop()
    servo_18.stop()
    GPIO.cleanup()
    print("Cleaned up GPIO")
