# Generated by Django 2.1.2 on 2020-05-11 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_item_sample_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='sample_1',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='サンプル項目1 文字列'),
        ),
    ]