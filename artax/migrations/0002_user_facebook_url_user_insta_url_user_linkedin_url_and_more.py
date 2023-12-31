# Generated by Django 4.2.4 on 2023-09-17 10:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("artax", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="facebook_url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="insta_url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="linkedin_url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="twitter_url",
            field=models.URLField(blank=True, null=True),
        ),
    ]
