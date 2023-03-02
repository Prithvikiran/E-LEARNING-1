from django.db import models
from base.models import User

class Todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    text = models.CharField(max_length=40)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text