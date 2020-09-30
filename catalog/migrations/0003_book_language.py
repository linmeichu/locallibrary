# Generated by Django 2.2.16 on 2020-09-30 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ManyToManyField(help_text='Select a language for this book', to='catalog.Language'),
        ),
    ]
