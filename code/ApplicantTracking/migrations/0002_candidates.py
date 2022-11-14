# Generated by Django 4.1.2 on 2022-10-17 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApplicantTracking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Score', models.IntegerField(default=0)),
                ('SourcedBy', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=100)),
                ('Status', models.CharField(max_length=50)),
                ('JobTitle', models.CharField(max_length=50)),
                ('SourcedFrom', models.CharField(max_length=50)),
                ('Mobile', models.IntegerField(default=0)),
            ],
        ),
    ]
