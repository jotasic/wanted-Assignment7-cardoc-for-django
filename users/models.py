from django.db                  import models
from django.contrib.auth.models import AbstractBaseUser

from .managers   import UserManager
from cars.models import Tire


class User(AbstractBaseUser):
    user_id    = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD  = 'user_id'

    def __str__(self):
        return f'{self.user_id}'

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
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    tire       = models.ForeignKey(Tire, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_actvate = models.BooleanField(default=True)

    class Meta:
        db_table = 'user_tires'