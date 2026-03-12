class User:
    def __init__(self, user_id, name, email, is_active=True):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.is_active = is_active


class Order:
    def __init__(self, order_id, user_id, total):
        self.order_id = order_id
        self.user_id = user_id
        self.total = total


class Notification:
    def __init__(self, recipient, message, channel="email"):
        self.recipient = recipient
        self.message = message
        self.channel = channel
