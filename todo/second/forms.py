from django import forms
from .models import Favourite, Todo


def min_length_3(value):
    if len(value) < 3:
        raise forms.ValidationError("3글자 이상 입력해주세요!")

class FavouriteForm(forms.Form):    
    name = forms.CharField(initial='홍길동', label="이름", validators=[min_length_3])
    url = forms.CharField(max_length=100)
    memo = forms.Textarea()

class FavouriteModelForm(forms.ModelForm):
    class Meta:
        model = Favourite
        fields = '__all__' #이건 전부다!
        #fields = ['name', 'address']일부만
        labels={
            'name':'명칭',
            'url':'주소',
            'memo':'메모',
            'group':'그룹'
            }
        
    #명칭, url ,메모, 그룹

class TodoForm(forms.Form):    
    name = forms.CharField(initial='홍길동', label="이름", validators=[min_length_3])
    status = forms.CharField(max_length=20)
    end_date = forms.DateField()
    del_yn = forms.BooleanField()
    #명칭 , 상태, 종료일, 그룹
    #저장

class TodoModelForm(forms.ModelForm):
    class Meta:
        model = Todo
        #fields = '__all__' #이건 전부다!
        fields = ['name', 'status', 'end_date', 'group']
        labels={
            'name':'명칭',
            'status':'상태',
            'end_date':'종료일',
            'group':'그룹'
        }

 