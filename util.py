import time
import datetime
import tensorflow as tf
from tensorflow.python.training import basic_session_run_hooks

class ProgressBarHook(basic_session_run_hooks.StepCounterHook):
    """Calculate and report time left during runtime."""

    def __init__(self,
                 max_steps,
                 every_n_steps=None,
                 every_n_secs=None):
        self._max_steps = max_steps
        self._agg_steps = 0

        super(ProgressBarHook, self).__init__(
            every_n_steps=every_n_steps,
            every_n_secs=every_n_secs,
            output_dir=None,
            summary_writer=None)

    def after_create_session(self, session, coord):
        self._started = time.time()
        global_step = session.run(self._global_step_tensor)
        self._timer.update_last_triggered_step(global_step)

    def _log_and_record(self, elapsed_steps, elapsed_time, global_step):
        steps_per_sec = elapsed_steps / elapsed_time

        self._agg_steps += elapsed_steps
        avg_steps_per_sec = self._agg_steps / (time.time() - self._started)

        steps_left = self._max_steps - global_step
        time_left = int(steps_left / avg_steps_per_sec)
        tf.logging.info('Global step %d/%d, Estimated time left: %s' %
                        (global_step, self._max_steps, datetime.timedelta(seconds=time_left)))


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


