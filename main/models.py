from django.db import models

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length = 100)
    added_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    category = models.ForeignKey(Type, on_delete = models.CASCADE)
    autors = models.CharField(max_length = 100) #default = 'default'
    pub_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

