# Generated by Django 3.1.7 on 2021-04-22 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('duration', models.IntegerField(default=0)),
                ('thumbnail', models.CharField(max_length=500)),
                ('video', models.CharField(max_length=500)),
                ('price', models.DecimalField(decimal_places=10, max_digits=11)),
                ('purchases', models.IntegerField(default=0)),
            ],
        ),
    ]
