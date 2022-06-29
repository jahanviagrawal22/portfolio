from django.shortcuts import render
from django.http import HttpResponse

exp=[
    {'post':'Google Cloud Intern','firm':'Google Cloud','disc':'Learnt Foundation of Google Cloud Computing and Fundamentals of Cloud Technology','time':''},
    {'post': 'Marketing Intern', 'firm': 'XYZ Solution',
        'disc': '','time':''}
    ]

ach=['Google Cloud Computing Foundation ','Google Cloud Computing','Digital Marketing']
edu=[{'college':"Jaipur Engineering College and Research Centre",'degree':"Bachelor of Technology",'course':"Computer Science",'gpa':'8.7','time':"August 2019 - June 2023"}]

def about(request):
    return render(request,'projects/about.html')


def achievements(request):
    return render(request, 'projects/achievements.html', {'ach': ach})

def education(request):
    return render(request,'projects/education.html', {'lest':edu})

def interests(request):
    return render(request,'projects/interests.html')

def personalProjects(request):
    return render(request,'projects/personalProjects.html',{'exp':exp})

def skills(request):
    return render(request,'projects/skills.html')