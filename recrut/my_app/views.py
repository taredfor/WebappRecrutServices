from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template.response import TemplateResponse

from .forms import UserForm, AnswerForm, AnswerForm2
from .models import Person, ObjectRecruts, ObjectsQuestion, ObjectsAnswers
from django import forms


# Create your views here.


def index(request):
    return render(request, "index.html")


def recrut_f(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            first_name = user_form.cleaned_data['f_name']
            second_name = user_form.cleaned_data['s_name']
            age = user_form.cleaned_data['age']
            mail_address = user_form.cleaned_data['mail_address']
            planet = user_form.cleaned_data['planet']
            person_id = add_new_person(first_name, second_name, age, mail_address, planet)
            return HttpResponseRedirect(f'/test/{person_id}')
    else:
        user_form = UserForm()
        return render(request, "for_f_recruter.html", {"form": user_form})


def test_f(request):
    answer_form2 = AnswerForm2()
    answer_form2.fields["test"] = forms.BooleanField()
    return render(request, "test123.html", context={"answer_form2": answer_form2})


def get_everything(request):
    person = Person.objects.all()
    return render(request, "get_everything.html", context={"person": person})


def add_new_person(f_name, s_name, age, mail_address, planet):
    # if request.method == 'POST':
    person = ObjectRecruts()
    person.f_name = f_name
    person.s_name = s_name
    person.age = age
    person.mail_address = mail_address
    person.planet = planet
    person.save()
    search_person = ObjectRecruts.objects.get(f_name=f_name, s_name=s_name)
    # print(search_person.id)
    return search_person.id


def get_question(request, person_id: int):
    if request.method == 'POST':
        questions = ObjectsQuestion.objects.all()
        person = ObjectRecruts.objects.get(id=person_id)
        person_name = person.f_name
        answer_form2 = AnswerForm2(request.POST)
        if answer_form2.is_valid():
            for q in questions:
                id_question = q.id
                answer = request.POST.dict()[q.questions]
                person = person_id
                add_answers_to_db(person, id_question, answer)
            #return HttpResponse(f"Пользователь добавлен {person_name} добавлен в систему")
            #return render(request, "add_user.html", context={"person_name": person_name})
            return HttpResponseRedirect(f'/add_user/{person_name}')
    questions = ObjectsQuestion.objects.all()
    answer_form2 = AnswerForm2()
    for q in questions:
        print(q.questions)
        print(q.id)
        answer_form2.fields[q.questions] = forms.ChoiceField(choices=((True, 'True'), (False, 'False')),
                              initial='', widget=forms.Select(), required=True)
        print(answer_form2.fields)
    return render(request, "for_f_test.html", context={"answer_form2": answer_form2, "person_id": person_id})


def add_answers_to_db(person: int, id_question: int, answer_que: bool):
    answer = ObjectsAnswers()
    answer.user_id = person
    answer.questions = id_question
    answer.answers = answer_que
    answer.save()

def all_users_list(request):
    persons = ObjectRecruts.objects.all()
    return render(request, "all_user_list.html", context={"persons": persons})

def return_list(request, person_name):
    return render(request, "add_user.html", context={"person_name": person_name})
