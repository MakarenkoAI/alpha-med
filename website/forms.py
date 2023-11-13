from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record, Room, WithAgeAndMale, WithDate, WithPatient
import mysite.settings as s
class SignUpForm(UserCreationForm):
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Имя'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Фамилия'}))

	class Meta(User):
		model = User
		fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<ul class="form-text text-muted small"><li>Пользователь с таким именем уже существует.</li><li>Обязательно. 150 символов и менее. Только буквы, цифры и @/./+/-/_ .</li></ul>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Ваш пароль не должен повторять ваши данные.</li><li>Пароль должен содержать 8 и более символов.</li><li>Пароль слишком легко угадать.</li><li>Пароль не должен состоять только из цифр.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<ul class="form-text text-muted"><li>Повторите раннее введенный пароль для верификации.</li></ul>'

class AddRecordForm(forms.ModelForm):
	last_name = forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Фамилия'}))
	first_name = forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Имя'}))
	father_name = forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Отчество'}))

	male = forms.ChoiceField(choices=Record.MALE, label='Пол:',widget=forms.Select(attrs={"name": "select_0","class": "form-control"}))
	databirth = forms.DateField(required=True, input_formats=s.DATE_INPUT_FORMATS, label="", widget=forms.DateInput(attrs={'class':'form-control', 'placeholder':'Дата рождения'}))
	diagnose = forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Диагноз'}))
	features = forms.CharField(required=False, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Особые приметы'}))

	data = forms.DateField(required=True, input_formats=s.DATE_INPUT_FORMATS, label="", widget=forms.DateInput(attrs={'class':'form-control', 'placeholder':'Дата поступления'}))
	palata = forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Номер палаты'}))
	phone = forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Телефонный номер'}))

	rest = forms.CharField(required=False, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Прочее'}))

	class Meta:
		model = Record
		exclude = ('user',)


class AddRoomForm(forms.ModelForm):
	patient = forms.ModelChoiceField(queryset=Record.objects.values_list('id',flat=True), label='ID пациента', widget=forms.Select(attrs={"name": "select_0","class": "form-control"}))
	data_in = forms.DateField(required=True, input_formats=s.DATE_INPUT_FORMATS, label='',widget=forms.DateInput(attrs={'class':'form-control', 'placeholder':'Дата поступления'}))
	data_out = forms.DateField(required=True, input_formats=s.DATE_INPUT_FORMATS, label ='',widget=forms.DateInput(attrs={'class':'form-control', 'placeholder':'Дата выписки'}))
	room = forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Номер палаты'}))
	phone_room = forms.CharField(required=False, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Телефон палаты'}))
	reason = forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Причина выписки'}))
	
	class Meta:
		model = Room
		exclude = ('user',)

class FindPatient(forms.ModelForm):
	#last_name = forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Фамилия'}))
	first_name = forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Имя'}))
	class Meta:
		model = WithPatient
		exclude = ('user',)

class FindDate(forms.ModelForm):
	data_in = forms.DateField(required=True, input_formats=s.DATE_INPUT_FORMATS, label='',widget=forms.DateInput(attrs={'class':'form-control', 'placeholder':'Дата поступления'}))
	class Meta:
		model = WithDate
		exclude = ('user',)

class FindAgeAndMale(forms.ModelForm):
	data_in = forms.DateField(required=True, input_formats=s.DATE_INPUT_FORMATS, label='',widget=forms.DateInput(attrs={'class':'form-control', 'placeholder':'Дата поступления'}))
	male = forms.ChoiceField(choices=Record.MALE, label='Пол:',widget=forms.Select(attrs={"name": "select_0","class": "form-control"}))
	class Meta:
		model = WithAgeAndMale
		exclude = ('user',)