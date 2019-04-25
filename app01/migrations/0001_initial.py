# Generated by Django 2.1.4 on 2019-04-22 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Press',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='press_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Press'),
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(to='app01.Book'),
        ),
    ]