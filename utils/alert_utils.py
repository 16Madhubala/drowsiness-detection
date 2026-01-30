from playsound import playsound
import threading

def play_alarm(path):
    threading.Thread(target=playsound, args=(path,), daemon=True).start()
