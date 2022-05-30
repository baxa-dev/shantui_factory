from django.db import models
from account.validators import PhoneValidator
from ckeditor.fields import RichTextField


class SpecialTechniqueCategory(models.Model):
    name = models.CharField(max_length=60, verbose_name="название")
    image = models.ImageField(upload_to='images/special_technique/', blank=True)
    top = models.IntegerField(default=1, null=True)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name = "Категория специальной техники"
        verbose_name_plural = "Категории специальной техники"


class SpecialTechnique(models.Model):
    category = models.ForeignKey('core.SpecialTechniqueCategory', on_delete=models.CASCADE, verbose_name="категория")
    name = models.CharField(max_length=100, verbose_name="название")
    description = RichTextField(blank=True, null=True, verbose_name="описание")
    description_bot = models.TextField(null=True, verbose_name="описание для бота")
    image = models.ImageField(upload_to="special_technique/", verbose_name="изображение")
    doc = models.FileField(upload_to="doc-st/", null=True, blank=True)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name = "Специальная техника"
        verbose_name_plural = "Специальной техники"


class Factory(models.Model):
    name = models.CharField(max_length=100, verbose_name="название")
    description = RichTextField(blank=True, null=True, verbose_name="описание")
    description_bot = models.TextField(blank=True, null=True, verbose_name="описание для бота")
    image = models.ImageField(upload_to="factory/", verbose_name="изображение")

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name = "Завод"
        verbose_name_plural = "Заводы"


class SpecialTechniqueApplication(models.Model):
    specialTechnique = models.ForeignKey("core.SpecialTechnique", on_delete=models.CASCADE,
                                         verbose_name="особая техника")
    user = models.ForeignKey("bot.BotUser", on_delete=models.CASCADE, verbose_name="Пользователь")

    def __str__(self) -> str:
        return str(self.user)


class FactoryApplication(models.Model):
    factory = models.ForeignKey("core.Factory", on_delete=models.CASCADE, verbose_name="завод")
    user = models.ForeignKey("bot.BotUser", on_delete=models.CASCADE, verbose_name="Пользователь")

    def __str__(self) -> str:
        return str(self.user)


class ServiceCenterRequest(models.Model):
    user = models.ForeignKey('bot.BotUser', on_delete=models.CASCADE, verbose_name="Пользователь")

    class Meta:
        verbose_name = "Запрос сервисного центра"
        verbose_name_plural = "Запросы в сервисный центр"


class Contact(models.Model):
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField("phone", max_length=20,
                             # validators=[PhoneValidator()]
                             )
    email = models.EmailField(max_length=70)
    messages = models.TextField(max_length=500)

    def __str__(self) -> str:
        return str(self.name)
