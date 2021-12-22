from django.db import models


# Create your models here.
class Categories(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class SubCategories(models.Model):
    category = models.ForeignKey(Categories, related_name='category', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Books(models.Model):
    sub_category = models.ForeignKey(SubCategories, related_name='sub_category', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year = models.IntegerField()
    cover = models.ImageField()
    language = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
