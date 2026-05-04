from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Purchase(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name