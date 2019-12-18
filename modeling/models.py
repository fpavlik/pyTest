from django.db import models

# Create your models here.
class Flower(models.Model):
    
    flower_name = models.CharField(max_length=20, help_text="Name of flower type")
    mass = models.IntegerField()
    consumption = models.IntegerField(help_text="How much food does it takes")
    lives = models.IntegerField(help_text="How long does it lives in tacts")
    sex_time = models.IntegerField(help_text="in which tact it can do some bad staff)))")
    seeds = models.IntegerField()
    position = models.ForeignKey('Square', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.flower_name

    # def __unicode__(self):
    #     return 

    def get_absolute_url(self):
        return reverse("flower_detail", kwargs={"pk": self.pk})
    
class Square(models.Model):
    
    mass = models.IntegerField()
    is_free = models.BooleanField()
    row = models.IntegerField()
    col = models.IntegerField()

    def __str__(self):
        return 

    # def __unicode__(self):
    #     return 

    def get_absolute_url(self):
        return reverse("flower_detail", kwargs={"pk": self.pk})

class Map(models.Model):
    
    size = models.IntegerField()

    def __str__(self):
        return 

    # def __unicode__(self):
    #     return 

    def get_absolute_url(self):
        return reverse("flower_detail", kwargs={"pk": self.pk})


