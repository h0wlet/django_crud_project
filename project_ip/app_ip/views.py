from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.template.response import TemplateResponse

from app_ip import forms, models


def home(request):
    return TemplateResponse(request, 'home.html')


def university_list(request):
    all_univers = models.University.objects.all()
    data = {'universities': all_univers}
    return TemplateResponse(request, 'university_list.html', data)


def create_university(request):
    form = forms.UniversityForm()

    if request.method == 'POST':
        form = forms.UniversityForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            models.University(full_name=cd['full_name'],
                              short_name=cd['short_name'],
                              date=cd['date']).save()

            return HttpResponseRedirect('/app_ip/universities/')

    data = {'form': form}
    return render(request, 'university.html', data)


def delete_university(request, univer_id):
    try:
        university = models.University.objects.get(id=univer_id)
        university.delete()
        return HttpResponseRedirect('/app_ip/universities/')
    except models.University.DoesNotExist:
        return HttpResponseNotFound("Университета с таким id не существует")


def update_university(request, univer_id):
    university = models.University.objects.get(id=univer_id)
    form = forms.UniversityForm(instance=university)

    if request.method == 'POST':
        form = forms.UniversityForm(request.POST, instance=university)
        if form.is_valid():
            cd = form.cleaned_data
            models.University.objects.filter(id=univer_id).update(full_name=cd['full_name'],
                                                                  short_name=cd['short_name'],
                                                                  date=cd['date'])
            return HttpResponseRedirect('/app_ip/universities/')

    data = {'form': form}
    return render(request, 'university.html', data)


def student_list(request):
    all_studs = models.Student.objects.all()
    data = {'students': all_studs}
    return TemplateResponse(request, 'student_list.html', data)


def create_student(request):
    form = forms.StudentForm()

    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            models.Student(name=cd['name'],
                           date_of_birth=cd['date_of_birth'],
                           institution=cd['institution'],
                           year=cd['year']).save()

            return HttpResponseRedirect('/app_ip/students/')

    data = {'form': form}
    return render(request, 'student.html', data)


def delete_student(request, stud_id):
    try:
        student = models.Student.objects.get(id=stud_id)
        student.delete()
        return HttpResponseRedirect("/app_ip/students/")
    except models.Student.DoesNotExist:
        return HttpResponseNotFound("Студента с таким id не существует")


def update_student(request, stud_id):
    student = models.Student.objects.get(id=stud_id)
    form = forms.StudentForm(instance=student)

    if request.method == 'POST':
        form = forms.StudentForm(request.POST, instance=student)
        if form.is_valid():
            cd = form.cleaned_data
            models.Student.objects.filter(id=stud_id).update(name=cd['name'],
                                                             date_of_birth=cd['date_of_birth'],
                                                             institution=cd['institution'],
                                                             year=cd['year'])
            return HttpResponseRedirect('/app_ip/students/')

    data = {'form': form}
    return render(request, 'student.html', data)
