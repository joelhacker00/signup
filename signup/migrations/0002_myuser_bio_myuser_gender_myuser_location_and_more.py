# Generated by Django 4.0.4 on 2022-04-26 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='bio',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='myuser',
            name='gender',
            field=models.CharField(choices=[('MA', 'Male'), ('FA', 'Female'), ('OT', 'Other')], default='Choose Gender', max_length=2),
        ),
        migrations.AddField(
            model_name='myuser',
            name='location',
            field=models.CharField(choices=[('ST', 'STOCKHOLM'), ('GO', 'GOTHENBURG'), ('UP', 'UPPSALA'), ('MA', 'MALMÖ')], default='Choose Location', max_length=2),
        ),
        migrations.AddField(
            model_name='myuser',
            name='profilepic',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
