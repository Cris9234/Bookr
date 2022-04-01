# Generated by Django 3.2.5 on 2022-03-18 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the Publisher.', max_length=50)),
                ('website', models.URLField(help_text='The publisher website.')),
                ('email', models.EmailField(help_text="The Publisher's email address.", max_length=254)),
            ],
        ),
    ]