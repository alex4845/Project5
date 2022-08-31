# Generated by Django 4.1 on 2022-08-17 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shtors', '0004_alter_list1_img_alter_list2_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='List3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='shtors/')),
                ('list2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shtors.list2')),
            ],
        ),
    ]