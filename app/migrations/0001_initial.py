# Generated by Django 5.1 on 2024-08-31 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('cadegoria', models.CharField(max_length=40)),
                ('descricao', models.TextField(max_length=300)),
                ('foto', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]
