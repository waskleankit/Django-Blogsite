# Generated by Django 4.0 on 2021-12-28 08:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BlogAdmin', '0014_alter_category_create_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 28, 8, 29, 1, 630196, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='category',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 28, 8, 29, 1, 630209, tzinfo=utc), verbose_name='date updated'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 28, 8, 29, 1, 629939, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='posts',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]