import factory

from usuarios.models import User


class UsuarioRegularFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "usuarios.User"
        django_get_or_create = ("username",)

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    username = factory.Faker("user_name")
    is_superuser = False

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)

        return manager.create_user(*args, **kwargs)


class UsuarioAdminFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "usuarios.User"
        django_get_or_create = ("username",)

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    username = factory.Faker("user_name")
    password = factory.Faker("password")
    is_superuser = True
    is_staff = True

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)

        return manager.create_superuser(*args, **kwargs)
