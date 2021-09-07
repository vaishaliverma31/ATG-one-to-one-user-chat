# Generated by Django 3.2 on 2021-09-07 05:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210907_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
        migrations.CreateModel(
            name='chatroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiveruser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiveruser', to=settings.AUTH_USER_MODEL)),
                ('senduser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='senduser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]