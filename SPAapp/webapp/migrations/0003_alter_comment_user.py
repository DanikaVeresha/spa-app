# Generated by Django 5.1.3 on 2024-11-29 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_rename_date_user_registerdate_remove_user_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='User',
            field=models.CharField(max_length=100),
        ),
    ]