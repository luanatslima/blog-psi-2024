# Generated by Django 5.1.1 on 2024-09-06 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_descricao_post_texto_remove_post_cadegoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='texto',
        ),
        migrations.AddField(
            model_name='post',
            name='conteudo',
            field=models.TextField(default='a', max_length=1200),
            preserve_default=False,
        ),
    ]
