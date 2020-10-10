# Generated by Django 2.2.15 on 2020-10-06 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services1', '0002_oneoff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yearly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.RenameModel(
            old_name='Packages',
            new_name='Monthly',
        ),
        migrations.RenameModel(
            old_name='OneOff',
            new_name='One',
        ),
    ]