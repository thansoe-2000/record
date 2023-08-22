from django import forms
from .models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        labels = {
            'name':'နာမေ',
            'age':'အသက်',
            'address':'နိန်ရပ်လိပ်စာ',
            'contact':'ဆက်သွယ်ရန် လိပ်စာ',
            'current_class':'လက်ဟိ အတန်း',
            'major':'အထူးပြု ဘာသာ',
            'image':'ဓါတ်ပုံ',

            'f_name':'အဖ နာမေ',
            'f_age':'အသက်',
            'f_careers':'အလုပ် အကိုင်',
            'f_address':'နိန်ရပ် လိပ်စာ',
            'f_contact':'ဆက်သွယ်ရန် လိပ်စာ',
            'f_image':'ဓါတ်ပုံ',

            'm_name':'အမိ နာမေ',
            'm_age':'အသက်',
            'm_careers':'အလုပ် အကိုင်',
            'm_address':'နိန်ရပ် လိပ်စာ',
            'm_contact':'ဆက်သွယ်ရန် လိပ်စာ',
            'm_image':'ဓါတ်ပုံ',
            
        }
        widgets = {
            'name':forms.TextInput(attrs=({'placeholder':'နာမေ ကို ရိုက်ထည့်ပါ'})),
            'age':forms.DateInput(attrs=({'placeholder':'အသက်ကို ရိုက်ထည့်ပါ', 'type':'date'})),
            'address':forms.TextInput(attrs=({'placeholder':'နိန်ရပ်လိပ်စာ ကို ရိုက်ထည့်ပါ'})),
            'contact':forms.TextInput(attrs=({'placeholder':'ဆက်သွယ်ရန်လိပ်စာ ကို ရိုက်ထည့်ပါ'})),
            'current_class':forms.TextInput(attrs=({'placeholder':'လက်ဟိအတန်း ကို ရိုက်ထည့်ပါ'})),
            'major':forms.TextInput(attrs=({'placeholder':'အထူးပြုဘာသာရပ် ကို ရိုက်ထည့်ပါ'})),
            'image':forms.FileInput(attrs=({})),

            'f_name':forms.TextInput(attrs=({'placeholder':'နာမေ ကို ရိုက်ထည့်ပါ'})),
            'f_age':forms.DateInput(attrs=({'placeholder':'အသက်ကို ရိုက်ထည့်ပါ', 'type':'date'})),
            'f_careers':forms.TextInput(attrs=({'placeholder':'အလုပ်အကိုင် ကို ရိုက်ထည့်ပါ'})),
            'f_address':forms.TextInput(attrs=({'placeholder':'နိန်ရပ်လိပ်စာ ကို ရိုက်ထည့်ပါ'})),
            'f_contact':forms.TextInput(attrs=({'placeholder':'ဆက်သွယ်ရန်လိပ်စာ ကို ရိုက်ထည့်ပါ'})),
            'f_image':forms.FileInput(attrs=({})),

            'm_name':forms.TextInput(attrs=({'placeholder':'နာမေ ကို ရိုက်ထည့်ပါ'})),
            'm_age':forms.DateInput(attrs=({'placeholder':'အသက်ကို ရိုက်ထည့်ပါ', 'type':'date'})),
            'm_careers':forms.TextInput(attrs=({'placeholder':'အလုပ်အကိုင် ကို ရိုက်ထည့်ပါ'})),
            'm_address':forms.TextInput(attrs=({'placeholder':'နိန်ရပ်လိပ်စာ ကို ရိုက်ထည့်ပါ'})),
            'm_contact':forms.TextInput(attrs=({'placeholder':'ဆက်သွယ်ရန်လိပ်စာ ကို ရိုက်ထည့်ပါ'})),
            'm_image':forms.FileInput(attrs=({})),



        }


    