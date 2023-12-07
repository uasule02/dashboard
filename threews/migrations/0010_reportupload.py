# Generated by Django 4.2.7 on 2023-12-01 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('threews', '0009_customuser_user_sector'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('open', 'Open'), ('closed', 'Closed')], max_length=10)),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='threews.month')),
                ('sectors', models.ManyToManyField(to='threews.sector')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='threews.year')),
            ],
        ),
    ]