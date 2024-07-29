from django.db import models

# Create your models here.
class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=30)
    categari = models.CharField(max_length=60, default='')
    subcategari = models.CharField(max_length=60, default='')
    price = models.IntegerField(default=0)
    product_des = models.CharField(max_length=300)
    issue_date = models.DateField()
    image = models.ImageField(upload_to='msc/images', default='')

    def __str__(self) -> str:
        return self.product_name
    

class contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=60, default='')
    phno = models.IntegerField(max_length=60, default='')
    des = models.CharField(max_length=600, default='')

    def __str__(self) -> str:
        return self.name