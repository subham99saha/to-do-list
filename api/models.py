from django.db import models

# Create your models here.
class todo(models.Model):

   task = models.CharField(max_length = 300)
   status = models.BooleanField(default = False)

   class Meta:
      db_table = "todo"
