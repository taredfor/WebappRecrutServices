# Generated by Django 4.2 on 2023-05-17 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0007_alter_objectsanswers_answers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectsanswers',
            name='questions',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='my_app.objectsquestion'),
        ),
    ]
