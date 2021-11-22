from django.db import models


class Tire(models.Model):
    width        = models.PositiveSmallIntegerField()
    wheel_size   = models.PositiveSmallIntegerField()
    aspect_ratio = models.PositiveSmallIntegerField()
    created_at   = models.DateTimeField(auto_now=True)
    updated_at   = models.DateTimeField(auto_now_add=True)
    is_actvate   = models.BooleanField(default=True)

    class Meta:
        db_table = 'tires'