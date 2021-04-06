# Generated by Django 3.1.7 on 2021-04-06 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20210403_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_coffee',
            name='categories',
            field=models.CharField(choices=[('C', 'Coffee'), ('IC', 'Iced Coffee'), ('E', 'Espresso'), ('C', 'Cappucino')], default='C', max_length=2, verbose_name='Categories'),
        ),
        migrations.AlterField(
            model_name='user_coffee',
            name='categories',
            field=models.CharField(choices=[('C', 'Coffee'), ('IC', 'Iced Coffee'), ('E', 'Espresso'), ('C', 'Cappucino')], default='C', max_length=2, verbose_name='Categories'),
        ),
    ]