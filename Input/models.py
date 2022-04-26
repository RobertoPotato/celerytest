from django.db import models

# Create your models here.
class DataInput(models.Model):
    class Meta:
        db_table = "input_data"
    
    data = models.CharField(max_length=50)
    run_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.data


class TaskExecution(models.Model):
    task = models.ForeignKey(DataInput, on_delete=models.CASCADE)
    execution_date = models.DateField(auto_now = True)