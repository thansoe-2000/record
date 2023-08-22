from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CategoryForm(forms.ModelForm):
   class Meta:
      model = Category
      fields = "__all__"
      labels = {
         'user':'User Name',
         'name':'Category Name',

         
         }

      widgets = {
         'user':forms.Select(attrs=({'placeholder':'Select User'})),
         'name':forms.TextInput(attrs=({'placeholder':'Enter Category Name'})),
      }
class PhotoForm(forms.ModelForm):
   class Meta:
      model = Photo
      fields = "__all__"
      labels = {
         'category':'Category',
         'title':'Title',
         'country':'Country',
         'image':'Image'
      }
      widgets = {
         'category':forms.Select(attrs=({'placeholder':'Select Category'})),
         'title':forms.TextInput(attrs=({'placeholder':'Title'})),
         'country':forms.TextInput(attrs=({'placeholder':'Country'})),
         'image':forms.FileInput(attrs=({})),

      }

class CustomUserCreationForm(UserCreationForm):
   class Meta:
      model = User
      fields = [
         'username', 'password1', 'password2'
      ]
   def __init__(self, *args, **kwargs):
      super(CustomUserCreationForm, self).__init__(*args, **kwargs)
      self.fields['username'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter username'})
      self.fields['password1'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter password'})
      self.fields['password2'].widget.attrs.update({'class':'form-control', 'placeholder':'Confirm entered password'})


class NationForm(forms.ModelForm):
   class Meta:
      model = Nation
      fields = "__all__"
      labels = {
        'name':'လူမျိုး နာမေ',
       }
      widgets = {
         'name':forms.TextInput(attrs=({'placeholder':'လူမျိုးနာမေ ရိုက်ထည့်ပါ'}))
      }

class DepartmentForm(forms.ModelForm):
   class Meta:
      model = Department
      fields = "__all__"
      labels = {
         'name':'လက်ဟိ တာဝန်ထမ်းဆောင်နိန်ရေ ဌာန'
      }
      widgets = {
         'name':forms.TextInput(attrs=({'placeholder':'တာဝန်ထမ်းဆောင်နိန်ရေ ဌာနကိုရိုက်ထည့်ပါ'}))
      }

class ReligionForm(forms.ModelForm):
   class Meta:
      model = Religion
      fields = "__all__"
      labels = {
         'name':'ကိုးကွယ်ရေ ဘာသာ'
      }
      widgets = {
         'name':forms.TextInput(attrs=({'placeholder':'ကိုးကွယ်ရေ ဘာသာ ကိုရိုက်ထည့်ပါ'}))
      }

class TrainingGroundForm(forms.ModelForm):
   class Meta:
      model = TrainingGround
      fields = "__all__"
      labels = {
         'name':'သင်တန်း နိန်ရာ'
      }
      widgets = {
         'name':forms.TextInput(attrs=({'placeholder':'သင်တန်း နိန်ရာရိုက်ထည့်ပါ'}))
      }
        
class TrainingTypeForm(forms.ModelForm):
   class Meta:
      model = TrainingType
      fields = "__all__"
      labels = {
         'name':'သင်တန်းအမျိုးအစား'
      }
      widgets = {
         'name':forms.TextInput(attrs=({'placeholder':'သင်တန်း အမျိုးအစားရိုက်ထည့်ပါ'}))
      }

class RankForm(forms.ModelForm):
   class Meta:
      model = Rank
      fields = "__all__"
      labels = {
         'name':'အဆင့်'
      }
      widgets = {
         'name':forms.TextInput(attrs=({'placeholder':'အဆင့် ကို ရိုက်ထည့်ပါ'}))
      }

class AppointmentForm(forms.ModelForm):
   class Meta:
      model = Appointment
      fields = "__all__"
      labels = {
         'name':'တာဝန် နာမေ'
      }
      widgets = {
         'name':forms.TextInput(attrs=({'placeholder':'တာဝန် နာမေ ရိုက်ထည့်ပါ'}))
      }



class BloodForm(forms.ModelForm):
   class Meta:
      model = Blood
      fields = "__all__"
      labels = {
         'name':'သွီးအမျိုးအစား နာမေ'
      }
      widgets = {
         'name':forms.TextInput(attrs=({'placeholder':'သွီးအမျိုးအစား နာမေ ရိုက်ထည့်ပါ'}))
      }

class MarriedForm(forms.ModelForm):
   class Meta:
      model = Married
      fields = "__all__"
      labels = {
         'name':'အိမ်ထောင် ဟိ/မဟိ'
      }
      widgets = {
         'name':forms.TextInput(attrs=({'placeholder':'အိမ်ထောင် ဟိ/မဟိ ရိုက်ထည့်ပါ'}))
      }

class GenderForm(forms.ModelForm):
   class Meta:
      model = Gender
      fields = "__all__"
      labels = {
         'name':'လိင် အမျိုးအစား'
      }
      widgets = {
         'name':forms.TextInput(attrs=({'placeholder':'လိင် အမျိုးအစား ရိုက်ထည့်ပါ'}))
      }

class CrimeForm(forms.ModelForm):
   class Meta:
      model = Crime
      fields = "__all__"
      labels = {
         'name':'နာမေ',
         'crime_type':'ပြစ်မှု အမျိုးအစား',
         'punished':'ပြစ်ဒဏ်',
         'start':'ပြစ်ဒဏ် စရေနိန့်',
         'end':'ပြစ်ဒဏ် ဆုံးရေနိန့်',
         'commander':'အထက်လူကြီး',
      }

      widgets = {
      'name':forms.Select(attrs=({'placeholder':'နာမေ'})),

      'crime_type':forms.TextInput(attrs=({'placeholder':'ပြစ်မှု အမျိုးအစားရိုက်ထည့်ပါ'})),
      'punished':forms.TextInput(attrs=({'placeholder':'ပြစ်ဒဏ် အမျိုးအစားရိုက်ထည့်ပါ', })),
      'start':forms.DateInput(attrs=({'placeholder':'ပြစ်ဒဏ် စရေနိန့်ကို ရိုက်ထည့်ပါ', 'type':'date'})),
      'end':forms.DateInput(attrs=({'placeholder':'ပြစ်ဒဏ် ဆုံးရေနိန့်ကို ရိုက်ထည့်ပါ', 'type':'date'})),
      'commander':forms.TextInput(attrs=({'placeholder':'အထက်လူကြီး နာမေ ကို ရိုက်ထည့်ပါ'})),

      }
        
class PersonalForm(forms.ModelForm):
   class Meta:
      model = Personal
      fields = "__all__"
      labels = {
         'name':'နာမေ',
         'rank':'အဆင့်',
         'appointment':'တာဝန်',
         'ser_number':'ကိုယ်ပိုင် နံပါတ်',
         'image':'ဓါတ်ပုံ',
         'department':'ဌာန',
         'gender':'လိင်',
         'birhday':'မွီးနိ့',
         'religion':'ကိုးကွယ်ရေ ဘာသာ',
         'nation':'လူမျိုး',
         'address':'နိန်ရပ် လိပ်စာ',
         'father':'အဖ နာမေ',
         'mother':'အမိ နာမေ',
         'married':'အိမ်ထောင် ဟိ/မဟိ',
         'blood':'သွီး အမျိုးအစား',
         'health':'ကျန်းမာရီး',
         'height':'အရပ်',
         'education':'ပညာ အရည်အခြင်း',
         'join_date':'တပ်ဝင် ရက်စွဲ',
         'batch_no':'သင်တန်း အပါတ်စဥ်',
         'trained_place':'သင်တန်း နိန်ရာ',
         'trained_type':'တက်ရောက်ဖူးရေ သင်တန်း',
         'long_time':'သင်တန်းကြာချိန်'
         
        
      }

      widgets = {
         'name':forms.TextInput(attrs=({'placeholder':'နာမေ ကိုရိုက်ထည့်ပါ'})),
         'rank':forms.Select(attrs=({'placeholder':'အဆင့် ကိုရွီးချယ်ပါ'})),
         'appointment':forms.Select(attrs=({'placeholder':'တာဝန် ကိုရွီးချယ်ပါ'})),
         'ser_number':forms.TextInput(attrs=({'placeholder':'ကိုယ်ပိုင် နံပါတ် ကိုရိုက်ထည့်ပါ'})),
         'image':forms.FileInput(attrs=({})),
         'department':forms.Select(attrs=({'placeholder':'ဌာန ကိုရွီးချယ်ပါ'})),
         'gender':forms.Select(attrs=({'placeholder':'လိင် အမျိုးအစား ကိုရိုက်ထည့်ပါ'})),
         'birthday':forms.DateInput(attrs=({'placeholder':'မွီးနိ့ ကိုရိုက်ထည့်ပါ', 'type':'date'})),
         'religion':forms.Select(attrs=({'placeholder':'ကိုးကွယ်ရေဘာသာ ကိုရိုက်ထည့်ပါ'})),
         'nation':forms.Select(attrs=({'placeholder':'လူမျိုး ကိုရိုက်ထည့်ပါ'})),
         'address':forms.TextInput(attrs=({'placeholder':'လိပ်စာ ကိုရိုက်ထည့်ပါ'})),
         'father':forms.TextInput(attrs=({'placeholder':'အဖ နာမေ ကိုရိုက်ထည့်ပါ'})),
         'mother':forms.TextInput(attrs=({'placeholder':'အမိ နာမေ ကိုရိုက်ထည့်ပါ'})),
         'married':forms.Select(attrs=({'placeholder':'အိမ်ထောင် ဟိ/မဟိ ကိုရိုက်ထည့်ပါ'})),
         'blood':forms.Select(attrs=({'placeholder':'သွီးအမျိုးအစား ကိုရွီးချယ်ပါ'})),
         'health':forms.TextInput(attrs=({'placeholder':'ကျန်းမာရီး ကိုရိုက်ထည့်ပါ'})),
         'height':forms.TextInput(attrs=({'placeholder':'အရပ် ကိုရိုက်ထည့်ပါ'})),
         'education':forms.TextInput(attrs=({'placeholder':'ပညာအရည်အခြင်း ကိုရိုက်ထည့်ပါ'})),
         'join_date':forms.DateInput(attrs=({'placeholder':'တပ်ဝင် ရက်စွဲ ကိုရိုက်ထည့်ပါ', 'type':'date'})),
         'batch_no':forms.TextInput(attrs=({'placeholder':'သင်တန်းအမှတ်စဥ် ကိုရိုက်ထည့်ပါ'})),
         'trained_place':forms.Select(attrs=({'placeholder':'သင်တန်း နိန်ရာ ကိုရွီးချယ်ပါ'})),
         'trained_type':forms.SelectMultiple(attrs=({'placeholder':'သင်တန်း အမျိုးအစား ကိုရွီးချယ်ပါ'})),
         'long_time':forms.TextInput(attrs=({'placeholder':'သင်တန်း ကြာချိန် ကိုရိုက်ထည့်ပါ'})),

        
        
         
      }

      def __init__(self,*args, **kwargs):
        super(PersonalForm, self).__init__(*args, **kwargs)
        self.fields['rank'].empty_label = 'အဆင့် အမျိုးအစား ရွီးချယ်ပါ...'
        self.fields['appointment'].empty_label = 'တာဝန် အမျိုးအစား ရွီးချယ်ပါ...'
        self.fields['religion'].empty_label = 'ကိုးကွယ်ရေ ဘာသာ ရွီးချယ်ပါ...'
        self.fields['nation'].empty_label = 'လူမျိုး ရွီးချယ်ပါ...'
        self.fields['blood'].empty_label = 'သွီးအမျိုးအစား ီးချယ်ပါ...'
        self.fields['trained_place'].empty_label = 'သင်တန်း နိန်ရာ ရွီးချယ်ပါ...'
        self.fields['trained_type'].empty_label = 'သင်တန်း အမျိုးအစား ရွီးချယ်ပါ...'
       
class Serviced_Form(forms.ModelForm):
   class Meta:
      model = ServicedPlace
      fields = "__all__"
      labels = {
         'name':'နာမေ',
         'serviced':'ဌာန နာမေ',
         'start_date':'စရေ နိန့်',
         'end_date':'ဆုံးရေ နိန့်',
         'long_time':'ကြာချိန်'
      }

      widgets = {
         'name':forms.Select(attrs=({'placeholder':'နာမေ ကို ရွီးချယ်ပါ'})),
         'serviced':forms.Select(attrs=({'placeholder':'ဌာန နာမေ ကို ရိုက်ထည့်ပါ'})),
         'start_date':forms.DateInput(attrs=({'placeholder':'စရေ နိန့်', 'type':'date'})),
         'end_date':forms.DateInput(attrs=({'placeholder':'ဆုံးရေနိန့် ရွီးချယ်ပါ', 'type':'date'})),
         'long_time':forms.DateInput(attrs=({'placeholder':'ကြာချိန်'})),
      }
      def __init__(self,*args, **kwargs):
        super(PersonalForm, self).__init__(*args, **kwargs)
        self.fields['serviced'].empty_label = 'အဆင့် အမျိုးအစား ရွီးချယ်ပါ...'