from django.db import models

class HeroSection(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    description = models.TextField()
    profile_image = models.ImageField(upload_to='media/hero_images/')

    def __str__(self):
        return self.name
class Skill(models.Model):
    skill_name = models.CharField(max_length=100)
    logo_url= models.URLField(max_length=200)

    def __str__(self):
        return self.skill_name
