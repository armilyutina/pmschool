from django.shortcuts import render
import json
from .forms import EmailPostForms
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def enter(request):
    if request.method == 'GET':
        return render(request, 'enter/enter.html')
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode())
            forms = EmailPostForms(data)
            print(forms.errors)
            if forms.is_valid():
                subject = 'Поступление'
                name = data['name']
                school = data['school']
                town = data['town']
                classNumber = data['classNumber']
                phone = data['phoneNumber']
                email = data['email']
                message = 'ФИО: ' + str(name) + '\n' + 'Город: ' + str(town) + '\n' + 'Телефон: ' + str(phone) + '\n' + 'Класс поступления: ' + str(classNumber) + '\n' + 'Почта: ' + str(email)
                send_mail(subject, message, settings.EMAIL_HOST_USER, ['fmsmai2020@gmail.com'])
                return render(request, 'enter/enter.html')
            else:
                forms = EmailPostForms()
                return render(request, 'enter/enter.html')
        except ValueError:
            return JSONResponse({
                'error': 'NotSendMessage',
            })
        # forms = EmailPostForms(request.POST)
        # print(forms.errors)
        # if True:
        #     subject = 'Поступление'
        #     name = request.POST.get('name')
        #     school = request.POST.get('school')
        #     town = request.POST.get('town')
        #     clas = request.POST.get('classNumber')
        #     phone = request.POST.get('phoneNumber')
        #     email = request.POST.get('email')
        #     message = 'ФИО: ' + str(name) + '\n' + 'Город: ' + str(town) + '\n' + 'Телефон: ' + str(phone) + '\n' + 'Класс поступления: ' + str(clas) + '\n' + 'Почта: ' + str(email)
        #     send_mail(subject, message, settings.EMAIL_HOST_USER, ['fmsmai2020@gmail.com'])
        #     return render(request, 'enter/enter.html')
