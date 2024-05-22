from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

class Member(AbstractUser):
    username = models.CharField(max_length=30, unique=True,)
    groups = models.ManyToManyField(
        'auth.Group', related_name='user_members', blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='user_members', blank=True
    )

    USERNAME_FIELD = 'username'

    def save(self, *args, **kwargs):
        # Хешуємо пароль лише якщо він не був вже хешований
        if not self.password.startswith(('pbkdf2_sha256$', 'argon2')):
            self.password = make_password(self.password)
        super(Member, self).save(*args, **kwargs)

    def __str__(self):
        return self.get_full_name()
