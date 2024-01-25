import threading
import queue

class ProducerThread(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        for i in range(5):
            self.queue.put(i)
            print(f"Produced: {i}")

class ConsumerThread(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            try:
                item = self.queue.get(timeout=1)  # Wait for 1 second
                print(f"Consumed: {item}")
                self.queue.task_done()
            except queue.Empty:
                break

# Create a queue
my_queue = queue.Queue()

# Create producer and consumer threads
producer_thread = ProducerThread(my_queue)
consumer_thread = ConsumerThread(my_queue)

# Start the threads
producer_thread.start()
consumer_thread.start()

# Wait for threads to finish
producer_thread.join()
consumer_thread.join()

print("All threads have finished.")

