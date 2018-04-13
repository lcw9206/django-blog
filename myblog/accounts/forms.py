# accounts/forms.py

from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth import get_user_model
from django import forms


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True, label='이메일')
    profile_thumbnail = forms.ImageField(required=False, label='프로필 사진')

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', )  # User 모델의 email 필드 이용

    # clean_필드명 메서드를 이용해 각 필드의 유효성 검증 실시
    def clean_email(self):
        email = self.cleaned_data.get('email')
        User = get_user_model()

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('이미 등록된 이메일입니다.')
        return email

    def save(self):
        user = super().save()
        Profile.objects.create(
            user=user,
            profile_thumbnail=self.cleaned_data['profile_thumbnail'],
            )
        return user


class ProfileForm(forms.ModelForm):
    about = forms.CharField(label='자기소개', required=False, widget=forms.Textarea(attrs={
            'row': 50,
            'placeholder': '100자 이하로 등록해주세요'
    }))

    class Meta:
        model = Profile
        fields = ['about', 'profile_thumbnail']

    def clean_profile_thumbnail(self):
        profile_thumbnail = self.cleaned_data.get('profile_thumbnail', False)
        if not profile_thumbnail:
            profile_thumbnail = None
        return profile_thumbnail
