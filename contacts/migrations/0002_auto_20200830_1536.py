# Generated by Django 2.2.15 on 2020-08-30 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='listing_id',
            field=models.IntegerField(),
        ),
    ]
