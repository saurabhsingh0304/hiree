from django.db import models
from accounts.models import CustomUser

# Create your models here.


class ModelBase(models.Model):
    active = models.BooleanField(default=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, )
    added_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tag(ModelBase):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
