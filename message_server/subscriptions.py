
import asyncio

class SubscriptionPublisher(object):
    def __init__(self):
        self.subscriptions = set()

    def publish(self, message):
        for queue in self.subscriptions:
            queue.put_nowait(message)


class Subscription(object):
    def __init__(self, publisher):
        self.publisher = publisher
        self.queue = asyncio.Queue()
    
    def __enter__(self):
        self.publisher.subscriptions.add(self.queue)
        return self.queue

    def __exit__(self, type, value, traceback):
        self.publisher.subscriptions.remove(self.queue)
    

