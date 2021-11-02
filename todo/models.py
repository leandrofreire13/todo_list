from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_created=True)
    last_modifies = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
