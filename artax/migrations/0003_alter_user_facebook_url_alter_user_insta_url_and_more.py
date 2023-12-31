# Generated by Django 4.2.4 on 2023-09-17 11:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("artax", "0002_user_facebook_url_user_insta_url_user_linkedin_url_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="facebook_url",
            field=models.URLField(default="#"),
        ),
        migrations.AlterField(
            model_name="user",
            name="insta_url",
            field=models.URLField(default="#"),
        ),
        migrations.AlterField(
            model_name="user",
            name="linkedin_url",
            field=models.URLField(default="#"),
        ),
        migrations.AlterField(
            model_name="user",
            name="twitter_url",
            field=models.URLField(default="#"),
        ),
    ]
