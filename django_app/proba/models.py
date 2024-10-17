from django.db import models

# Create your models here.
class Patients(models.Model):
    patient_id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    value = models.PositiveIntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'score1'