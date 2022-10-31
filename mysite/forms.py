from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget
from django import forms


class ContactForm(forms.Form):
    """お問い合わせページ用フォーム"""

    name = forms.CharField(max_length=100, label="名前")
    email = forms.EmailField(max_length=100, label="メールアドレス")
    message = forms.CharField(label="メッセージ", widget=forms.Textarea())
    captcha = ReCaptchaField(widget=ReCaptchaWidget())
