# Generated by Django 5.2 on 2025-06-01 15:30

import Edahiras.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Edahiras', '0007_alter_audio_audio_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='audio_file',
            field=models.FileField(blank=True, help_text='Fichier audio au format MP3, WAV, OGG ou M4A (max. 20 MB)', null=True, upload_to='media/audio/', validators=[Edahiras.utils.validate_audio_file]),
        ),
    ]
