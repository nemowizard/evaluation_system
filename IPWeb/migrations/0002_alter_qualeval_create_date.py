# Generated by Django 4.2 on 2024-05-15 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IPWeb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualeval',
            name='create_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]