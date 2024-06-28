# Generated by Django 3.1 on 2024-06-18 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20240606_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_name',
            field=models.CharField(choices=[('Finance', 'Finance'), ('Monitoring and evaluation', 'Monitoring And Evaluation'), ('HR', 'Human Resource'), ('Community', 'Community'), ('Clinical', 'Clinical'), ('Operations', 'Operations'), ('Research', 'Research'), ('Communications', 'Communications'), ('Informatics and IT', 'Informatics and IT')], max_length=200, unique=True),
        ),
    ]
