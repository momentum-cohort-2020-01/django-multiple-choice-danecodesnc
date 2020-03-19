# Generated by Django 3.0.4 on 2020-03-19 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0008_auto_20200318_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashcard',
            name='deck',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='flashcards.Deck'),
        ),
    ]
