# Generated by Django 4.0.3 on 2022-09-12 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
