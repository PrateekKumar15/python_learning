import pyttsx3
import time
if __name__ == "__main__":
    engine = pyttsx3.init()
    while True:
        x = input("Enter what you want to speak")
        if x == "exit":
            break
        engine.say(x)
        engine.runAndWait()
        time.sleep(0.1)

