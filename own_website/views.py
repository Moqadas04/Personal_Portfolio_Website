from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from adminpanel.models import HeroSection   
from adminpanel.models import Skill
# Create your views here.
def index(request):
    all_skills = Skill.objects.all()
    hero=HeroSection.objects.first()
    context={
        'hero':hero,
        'all_skills':all_skills
    }
    return render(request, 'index.html',context)