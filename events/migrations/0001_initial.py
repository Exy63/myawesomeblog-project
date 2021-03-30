# Generated by Django 3.1.7 on 2021-03-30 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_image', models.ImageField(upload_to='event_images/')),
                ('event_text', models.CharField(max_length=300)),
            ],
        ),
    ]
