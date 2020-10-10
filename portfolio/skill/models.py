from django.db import models

class Myskill(models.Model):
    image=models.ImageField(upload_to='skillimage/')
    title=models.CharField(max_length=50,blank=False)
    desc=models.TextField(max_length=500,blank=True)
    datetime=models.DateTimeField(auto_now_add=False)    

    def __str__(self):
        return self.title
                     

