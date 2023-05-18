from django import forms


class UserForm(forms.Form):
    f_name = forms.CharField(max_length=10, label="First name")
    s_name = forms.CharField(max_length=15, label="Second name")
    age = forms.IntegerField(label="age")
    mail_address = forms.EmailField(label="mail address")
    planet = forms.CharField(label="Planet", required=True)

#Добавляю форму для ответа
class AnswerForm(forms.Form):
    question = forms.CharField(max_length=50)
    answer = forms.BooleanField()

class AnswerForm2(forms.Form):
    pass

