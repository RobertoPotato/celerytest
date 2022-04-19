from django.db import models

# Create your models here.
class DataInput(models.Model):
    class Meta:
        db_table = "input_data"
    
    data = models.CharField(max_length=50)

    def __str__(self):
        return self.data