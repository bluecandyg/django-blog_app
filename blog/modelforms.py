from django import forms
from .models import Post

# validator 함수 정의
def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력 해 주세요.')

# 모델 폼
class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']

# 기본 폼
class PostForm(forms.Form):
    title = forms.CharField(validators=[min_length_3_validator])
    text = forms.CharField(widget=forms.Textarea)

