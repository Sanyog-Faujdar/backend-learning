# Protocols and Duck Typing

from typing import Protocol

class Notifier(Protocol):
    def send(self,message: str) -> None:
        ...
    
class EmailNotifier:
    def send(self,message: str) -> None:
        print(f"sending email: {message}")

class SMSNotifier:
    def send(self,message: str) -> None:
        print(f"sending SMS: {message}")

class PushNotifier:
    def send(self, message: str) -> None:
        print(f"Sending push notification: {message}")

def notify_user(notifier: Notifier, message: str) -> None:
    notifier.send(message)

email = EmailNotifier()
sms = SMSNotifier()

notify_user(email, "Hello Alice")
notify_user(sms, "Hello Alice")

push = PushNotifier()
notify_user(push, "Hello Alice")