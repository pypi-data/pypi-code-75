# Generated by Django 2.2.2 on 2019-10-29 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("drc_cmis", "0002_auto_20190523_1054"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cmisconfig",
            name="client_url",
            field=models.URLField(
                default="http://localhost:8082/alfresco/api/-default-/public/cmis/versions/1.1/browser"
            ),
        ),
    ]
