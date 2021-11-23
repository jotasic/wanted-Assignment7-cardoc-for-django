from django.db                  import models
from django.contrib.auth.models import AbstractBaseUser

from .managers   import UserManager
from cars.models import Tire


class User(AbstractBaseUser):
    pk_id      = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    id         = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD  = 'id'

    def __str__(self):
        return f'{self.id}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        db_table = 'users'


class UserTire(models.Model):
    pk_id      = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    tire       = models.ForeignKey(Tire, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_actvate = models.BooleanField(default=True)

    class Meta:
        db_table = 'user_tires'