import time

class PerformanceTimers:
    def __init__(self):
        self.m_WorkerThreadTimers = {}

    def StartTimer(self, thread_name):
        self.m_WorkerThreadTimers[thread_name] = time.time()

    def StopTimer(self, thread_name):
        if thread_name in self.m_WorkerThreadTimers:
            elapsed_time = time.time() - self.m_WorkerThreadTimers.pop(thread_name)
            print(f"Thread {thread_name} elapsed time: {elapsed_time:.4f} seconds")
        else:
            print(f"Timer for thread {thread_name} not found")
