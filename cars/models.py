from django.db import models


class Tire(models.Model):
    pk_id        = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    width        = models.PositiveSmallIntegerField()
    aspect_ratio = models.PositiveSmallIntegerField()
    wheel_size   = models.PositiveSmallIntegerField()
    created_at   = models.DateTimeField(auto_now=True)
    updated_at   = models.DateTimeField(auto_now_add=True)
    is_actvate   = models.BooleanField(default=True)

    class Meta:
        db_table = 'tires'