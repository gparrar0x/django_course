# Generated by Django 4.1.3 on 2023-01-12 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=264)),
                ('last_name', models.CharField(max_length=264)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
