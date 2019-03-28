import time
import datetime

class ProgressBar(object):
    def __init__(self, size, report_interval):
        self.size = size
        self.lastReported = time.time()
        self.started = self.lastReported
        self.report_interval = report_interval

    def time_to_report(self):
        return time.time() - self.lastReported > self.report_interval

    def report(self, current, additional_msg):
        now = time.time()

        if now - self.lastReported > self.report_interval:

            progress = 100 * float(current) / self.size

            size_left = self.size - current
            time_elapsed = now - self.started
            throughput = current / time_elapsed
            time_left = int(size_left / throughput)
            time_left = datetime.timedelta(seconds=time_left)

            print "Progress: %0.2f%%, Time left: %s, %s" % (progress, time_left, additional_msg)

            self.lastReported = now


