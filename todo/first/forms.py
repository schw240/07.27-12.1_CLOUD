from django import forms
from .models import Students


def min_length_3(value):
    if len(value) < 3:
        raise forms.ValidationError("3글자 이상 입력해주세요!")

class StudentForm(forms.Form):
    name = forms.CharField(initial='홍길동', label="이름", validators=[min_length_3])
    address = forms.CharField(max_length=10)
    email = forms.CharField(widget=forms.Textarea)


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__' #이건 전부다!
        #fields = ['name', 'address']일부만
        labels = {
            'name': '이름'
        }
        help_text = {
            'name': '이름을 입력해주세요'
        }