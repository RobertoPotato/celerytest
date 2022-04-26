from celery import shared_task
from datetime import datetime, date


# from billing.core import run_postpaid_billing, postpaid_due_procured
# from .views import add_new_input

from .models import DataInput, TaskExecution

def should_execute():
    today = date.today()
    print(today)
    te = TaskExecution.objects.filter(execution_date=today).first()
    if te:
        print("Already executed")
        return False
    else:
        print("Run task")
        return True

def save_task_execution(task):
    te = TaskExecution()
    te.task = task
    te.save()


# Create your views here.
def add_new_input():
    print("Adding New data")
    data = "DATA INPUT"
    di = DataInput(data=data)
    di.save()
    return di

def schedule_api():
    """insert_data_to_inputs_table"""
    print("Entering scheduler")
    # ? Check if the task should be inserted
    if should_execute():
        task = add_new_input()
        save_task_execution(task)
    else:
        print("Nothing was executed")
        # run_postpaid_billing()


def schedule_heartbeat():
    print("Im alive")