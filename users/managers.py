from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, user_id, password=None):
        if not id:
            raise ValueError('Users must have an id')

        user = self.model(user_id=user_id)

        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, password=None):
        user = self.create_user(user_id=user_id, password=password)

        user.is_admin     = True
        user.is_superuser = True
        user.save(using=self._db)
        return user