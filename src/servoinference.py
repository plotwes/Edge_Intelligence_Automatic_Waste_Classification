import cv2
import numpy as np
import RPi.GPIO as GPIO
import time
from tensorflow.keras.models import load_model

# Load your trained model
model = load_model('/home/pi/rifqi & zai/densenet_model.keras')

# Define your trash categories
categories = ["Anorganik", "B3", "Organik", "Residu"]

# Preprocess the image frame for prediction
def preprocess_image(image):
    # Resize the image to the model's input size (224x224)
    image_resized = cv2.resize(image, (224, 224))
    # Normalize the image (pixel values from [0, 255] to [0, 1])
    image_normalized = image_resized / 255.0
    # Expand dimensions to match the model's input shape (1, 224, 224, 3)
    return np.expand_dims(image_normalized, axis=0)

# GPIO setup
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

def move_servo(pwm, duty_cycle, duration):
    """
    Move the servo to a certain duty cycle for a specific duration.
    """
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(duration)
    pwm.ChangeDutyCycle(0)  # Stop the signal to avoid jitter

def set_servo_angle(pwm, angle):
    """
    Set the servo angle. This is a helper function to convert angle to duty cycle.
    """
    duty_cycle = (angle / 18) + 2.5
    move_servo(pwm, duty_cycle, 0.5)

# Initialize webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image")
        break

    # Preprocess the frame for prediction
    preprocessed_frame = preprocess_image(frame)

    # Perform prediction using the trained model
    predictions = model.predict(preprocessed_frame)

    # Get the predicted class and confidence
    predicted_class = np.argmax(predictions)
    predicted_label = categories[predicted_class]

    # Display the prediction on the frame
    display_text = f"Prediction: {predicted_label}"
    cv2.putText(frame, display_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    # Move servos based on the prediction
    if predicted_label == "Anorganik":
        set_servo_angle(servo_17, 0)
        set_servo_angle(servo_18, 90)

    elif predicted_label == "B3":
        set_servo_angle(servo_17, 90)
        set_servo_angle(servo_18, 0)

    elif predicted_label == "Organik":
        set_servo_angle(servo_17, 180)
        set_servo_angle(servo_18, 90)

    elif predicted_label == "Residu":
        set_servo_angle(servo_17, 90)
        set_servo_angle(servo_18, 180)

    # Show the frame with the classification result
    cv2.imshow("Trash Classification", frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources and close windows
cap.release()
cv2.destroyAllWindows()

# Clean up GPIO settings
GPIO.cleanup()
