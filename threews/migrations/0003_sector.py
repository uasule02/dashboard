# Generated by Django 4.2.5 on 2023-10-31 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threews', '0002_alter_uploadedfile_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('acronyms', models.CharField(max_length=50)),
            ],
        ),
    ]