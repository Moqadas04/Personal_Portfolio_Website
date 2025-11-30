from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from adminpanel.models import HeroSection
from adminpanel.models import Skill
# Create your views here.
def login(request):
    return render(request,'login.html')
def skill_control(request):
    # Get list of skills to show on the page
    all_skills = Skill.objects.all()

    if request.method == "POST":
        # Read simple form fields
        name = request.POST.get('skill_name')
        url = request.POST.get('logo_url')
        skill_id = request.POST.get('skill_id')

        # If skill_id is provided -> update the existing record
        if skill_id:
            # filter().update() is simple and will not raise if id not found
            Skill.objects.filter(id=skill_id).update(skill_name=name, logo_url=url)
            messages.success(request, f"Skill '{name}' updated.")
        else:
            # Otherwise create a new record
            Skill.objects.create(skill_name=name, logo_url=url)
            messages.success(request, f"Skill '{name}' created.")

        # Redirect back to the same page (Post/Redirect/Get)
        return redirect('skill_control')

    # For GET just render the template with skills
    return render(request, "skill_control.html", {"skills": all_skills})


# Edit
def edit_skill(request, id):
    skill_obj = get_object_or_404(Skill, id=id)

    if request.method == "POST":
        skill_obj.skill_name = request.POST.get('skill_name')
        skill_obj.logo_url = request.POST.get('logo_url')
        skill_obj.save()
        return redirect('skill_control')

    return render(request, "skill_control.html", {"skill": skill_obj})


# Delete
def delete_skill(request, id):
    skill_obj = get_object_or_404(Skill, id=id)
    skill_obj.delete()
    return redirect('skill_control')
def home(request):
    hero = HeroSection.objects.first()
    if request.method == "POST":
        full_name = request.POST.get("name")
        title = request.POST.get("title")
        description = request.POST.get("description")
        photo = request.FILES.get("photo")

        if hero:
            hero.name = full_name
            hero.title = title
            hero.description = description

            if photo:
                hero.profile_image = photo

            hero.save()
        else:
            HeroSection.objects.create(
                name=full_name,
                title=title,
                description=description,
                profile_image=photo
            )

        

    return render(request, "home.html", {"hero": hero})
def dashboard(request):
    return render(request, "dashboard.html")