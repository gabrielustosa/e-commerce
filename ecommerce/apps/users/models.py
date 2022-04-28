from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser precisa precisa estar como True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff precisa precisa estar como True')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    cpf = models.CharField(max_length=14)
    name = models.CharField('Nome', max_length=150)
    phone_number = models.CharField('Número de telefone', max_length=15)
    is_staff = models.BooleanField('Equipe', default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'cpf', 'phone_number']

    def __str__(self):
        return self.email

    def first_name(self):
        return self.name.split(' ')[0]


class Address(models.Model):
    name = models.CharField('Nome', max_length=100)
    postal_code = models.CharField('Código Postal', max_length=10)
    address = models.CharField('Endereço', max_length=150)
    number = models.CharField('Número', max_length=10)
    complement = models.CharField('Complemento', max_length=100)
    city = models.CharField('Cidade', max_length=50)
    state = models.CharField('Estado', max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
