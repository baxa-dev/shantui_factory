from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class BotUser(models.Model):
    telegram_id = models.IntegerField(unique=True, verbose_name="идентификатор телеграммы")
    first_name = models.CharField(max_length=60, null=True, blank=True, verbose_name="имя")
    last_name = models.CharField(max_length=60, null=True, blank=True, verbose_name="фамилия")
    phone_number = PhoneNumberField("телефонный номер")
    join_date = models.DateTimeField(auto_now_add=True, verbose_name="дате вступления")
    update_profile = models.DateTimeField(auto_now=True, verbose_name="обновить профиль")

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)

    @property
    def get_full_name(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = "Пользователь бота"
        verbose_name_plural = "Пользователи ботов"
