from django.db import models

# Create your models here.


class category(models.Model):
    name = models.CharField(max_length=30)


class Author(models.Model):
    info = models.TextField()


class Publishing_house(models.Model):
    name = models.CharField(max_length=30)


class Text(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    img_href = models.CharField(default='', max_length=500)
    CheckBox = models.BooleanField(default=True)
    # Selection = models.CharField(max_length=256)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    Info = models.ForeignKey(Author, on_delete=models.CASCADE)

    publishing_house = models.ManyToManyField(Publishing_house, through='Enrollment')


class Enrollment(models.Model):
    Text = models.ForeignKey(Text, on_delete=models.CASCADE)
    Publishing_house = models.ForeignKey(Publishing_house, on_delete=models.CASCADE)


