from django import forms
from django.forms import fields
from .models import Student

# class StudentForm(forms.Form):
#     first_name = forms.CharField(max_length=30, label="Your Name")
#     last_name = forms.CharField(max_length=30, label="Your Surname")
#     number = forms.IntegerField(required=False)


class StudentForm(forms.ModelForm):
    
    # overwrite label
    first_name = forms.CharField(label='Your Name')
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['first_name'].label = 'Your Name' 
    
    class Meta:
        model = Student
        fields = '__all__' # ['first_name', 'last_name']
        
