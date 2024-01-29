import multiprocessing
import time

class MyProcess(multiprocessing.Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f"Process {self.name} is running")

if __name__ == "__main__":
    # Create process instances
    process1 = MyProcess(name="Process 1")
    process2 = MyProcess(name="Process 2")

    # Start processes,
    process2.start()
    process1.start()

    # Wait for processes to finish
    process1.join()
    process2.join()
