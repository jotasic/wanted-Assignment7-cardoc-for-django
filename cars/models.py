from django.db import models


class Tire(models.Model):
    width        = models.CharField(max_length=4)
    aspect_ratio = models.CharField(max_length=2)
    wheel_size   = models.CharField(max_length=2)
    created_at   = models.DateTimeField(auto_now=True)
    updated_at   = models.DateTimeField(auto_now_add=True)
    is_actvate   = models.BooleanField(default=True)

    class Meta:
        db_table = 'tires'