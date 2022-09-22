from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000,blank=True, null=True)
    brand = models.CharField(max_length=50, blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/")
    price = models.FloatField()
    
    def __str__(self):
        return self.name
