from django.db import models

# Create your models here.
class KNTLword(models.Model):
    word_id = models.AutoField(primary_key=True, blank=True)
    word = models.TextField(unique=True)
    word_desc = models.TextField()

    class Meta:
        managed = False
        db_table = 'KNTLword'