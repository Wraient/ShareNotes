from django.db import models

# Create your models here.
class Colleges(models.Model):
    college_name = models.CharField(max_length=150)
    college_nickname = models.CharField(max_length=100)
    dte_code = models.IntegerField(blank= False, null= False)
    
    class Meta:
        verbose_name = "College"
        verbose_name_plural = "Colleges"

    def __str__(self):
        return f"{self.college_nickname} ({self.dte_code})"
    


# class Post(models.Model):
#     username = models.CharField(max_length=100)
#     college = models.CharField(max_length=100)
#     subject = models.CharField(max_length=100)
    

#     def __str__(self):
#         return self.name