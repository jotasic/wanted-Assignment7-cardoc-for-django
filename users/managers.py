from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, id, password=None):
        if not id:
            raise ValueError('Users must have an id')

        user = self.model(id=id)

        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, id, password=None):
        user = self.create_user(id=id, password=password)

        user.is_admin     = True
        user.is_superuser = True
        user.save(using=self._db)
        return user