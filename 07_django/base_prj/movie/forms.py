from django import forms
from .models import Movie


# class MovieForm(forms.Form):
#     title = forms.CharField(max_length=100)
#     title_eng = forms.CharField(max_length=100)
#     audience = forms.IntegerField()
#     open_date = forms.DateField(
#         widget=forms.widgets.DateInput(attrs={'type': 'date'})
#
#     )
#     genre=forms.CharField(max_length=100)
#     watch_grade = forms.CharField(max_length=100)
#     score = forms.FloatField()
#     poster_url = forms.CharField()
#     description = forms.CharField(widget=forms.Textarea())


class MovieModelForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__' # 이렇게 하거나, ['title', 'title_eng'] 이런 식으로 특정 컬럼만 받을 수도 있음.
        widgets ={
            'open_date': forms.DateInput(attrs={'type': 'date'}),
        }
