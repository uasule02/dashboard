# Generated by Django 4.2.5 on 2023-09-28 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedfile',
            name='file',
            field=models.FileField(upload_to='upload/3ws'),
        ),
    ]
