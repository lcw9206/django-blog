# accounts/forms.py

from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class SignupForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', ) # User 모델의 email 필드 이용

    def save(self):
        user = super().save()
        Profile.objects.create(user = user)
        return user
