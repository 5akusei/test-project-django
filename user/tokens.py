from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )
account_activation_token = TokenGenerator()

# https://github.com/django/django/blob/main/django/contrib/auth/tokens.py#L8
# https://forum.djangoproject.com/t/django-passwordresettokengenerator/5872