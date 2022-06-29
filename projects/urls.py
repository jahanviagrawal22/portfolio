from django.urls import path
from . import views

urlpatterns=[
    path('',views.about,name="about"),
    path('about/', views.about, name="projects"),
    path('achievements/', views.achievements, name="achievements"),
    path('education/', views.education, name="education"),
    path('interests/',views.interests,name="interests"),
    path('personalProjects/', views.personalProjects, name="personalProject"),
    path('skills/', views.skills, name="skills"),
    ]