from datetime import datetime as dt
import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "usuarios.User"
        django_get_or_create = ("username",)

    first_name = factory.Faker("first_name", locale="pt_BR")
    last_name = factory.Faker("last_name", locale="pt_BR")
    username = factory.Faker("user_name", locale="pt_BR")
    email = factory.LazyAttribute(
        lambda obj: "%s-%s@mail.com" % (obj.username, dt.timestamp(dt.now()))
    )
    password = factory.Faker("password")


class RegularUserFactory(UserFactory):
    is_superuser = False
    is_staff = False

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)

        return manager.create_user(*args, **kwargs)


class AdminUserFactory(UserFactory):
    is_superuser = True
    is_staff = True

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)

        return manager.create_superuser(*args, **kwargs)
