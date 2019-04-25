from django.db import models


class Publish(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=64)

    def __str__(self):

        return self.name

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=64)
    publish_id = models.ForeignKey(to='Publish', on_delete=models.CASCADE)

    def __str__(self):

        return self.book_name

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    books = models.ManyToManyField(to='Book')

    def __str__(self):

        return self.name

class User(models.Model):
    name=models.CharField(max_length=32,verbose_name='用户名')
    password=models.CharField(max_length=32,verbose_name='密码')

    def __str__(self):
        return self.name