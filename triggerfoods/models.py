from django.db import models

# Create your models here.
class TriggerFood(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    severity = models.IntegerField()
    note = models.TextField()
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-severity', 'name')