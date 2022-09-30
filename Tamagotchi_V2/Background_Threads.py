import threading
import schedule
import time


class scheduler_job:
    def __init__(self):
        super().__init__()

    def run_again(self, interval=1, rmv_thread=False):
        cease_continuous_run = threading.Event()
        self.statusis = rmv_thread

        class ScheduleThread(threading.Thread):
            print(f"Scheduled: the thing")

            @classmethod
            def run(cls):
                while not self.statusis:
                    schedule.run_pending()
                    time.sleep(interval)

        continuous_thread = ScheduleThread()
        continuous_thread.name = "thread_background"
        continuous_thread.start()

        return cease_continuous_run

    def plan_job(self):
        self.posture_job = schedule.every(2).minutes.do(self.consist_decrease).tag('alljobs')
        print(self.posture_job)
        self.activate()

    def consist_decrease(self):
        hchange = -12.5
        schange = -16
        hychange = -6
        print("Stats would decrease")

    def activate(self):
        # Start the background thread
        self.run_again()

    def end_scheduling(self, job_name):
        print(f"Canceling all jobs")
        print(f" Before clearing: {schedule.get_jobs()}")
        schedule.clear()
        print(f" After clearing: {schedule.get_jobs()}")