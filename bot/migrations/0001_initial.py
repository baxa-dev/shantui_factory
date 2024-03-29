# Generated by Django 3.2.2 on 2022-05-16 21:04

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.IntegerField(unique=True, verbose_name='идентификатор телеграммы')),
                ('first_name', models.CharField(blank=True, max_length=60, null=True, verbose_name='имя')),
                ('last_name', models.CharField(blank=True, max_length=60, null=True, verbose_name='фамилия')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='телефонный номер')),
                ('join_date', models.DateTimeField(auto_now_add=True, verbose_name='дате вступления')),
                ('update_profile', models.DateTimeField(auto_now=True, verbose_name='обновить профиль')),
            ],
            options={
                'verbose_name': 'Пользователь бота',
                'verbose_name_plural': 'Пользователи ботов',
            },
        ),
    ]
