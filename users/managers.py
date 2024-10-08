from django.contrib.auth.base_user import BaseUserManager
from rest_framework.exceptions import ParseError


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email=None, password=None, username=None, **extra_fields):
        if not (email or username):
            raise ParseError('Укажите email или никнейм')

        if email:
            email = self.normalize_email(email)

        if not username:
            username = email

        
        user = self.model(username=username, **extra_fields)
        if email:
            user.email = email

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, username=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)

        return self._create_user(
            email, password, username, **extra_fields
        )

    def create_superuser(self, email=None, password=None, username=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        return self._create_user(
            email, password, username, **extra_fields
        )