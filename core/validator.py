import phonenumbers
from django.core.exceptions import ValidationError


class PhoneValidator:
    requires_context = False

    @staticmethod
    def validate(value):
        try:
            item = phonenumbers.parse(value)
            if not phonenumbers.is_valid_number(item):
                return False
        except:
            return False
        return True

    def __call__(self, value):
        if not PhoneValidator().validate(value):
            raise ValidationError("Введите номер телефона правильно!")