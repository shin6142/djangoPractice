# Generated by Django 3.1.2 on 2021-12-12 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
