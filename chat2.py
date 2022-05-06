from apscheduler.schedulers.blocking import BlockingScheduler
from chat import send


sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(send, 'interval', seconds=5)

sched.start()