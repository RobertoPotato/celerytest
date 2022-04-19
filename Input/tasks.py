from celery import shared_task

# from billing.core import run_postpaid_billing, postpaid_due_procured
from .views import add_new_input

@shared_task(name="insert_data_to_inputs_table")
def new_inputs(*args, **kwargs):
    """insert_data_to_inputs_table"""
    print("Hello")
    add_new_input('hi')
    run_postpaid_billing()