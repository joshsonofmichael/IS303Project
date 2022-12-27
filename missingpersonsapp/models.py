from django.db import models

# Create your models here.
class Missing_Person(models.Model):
    date_missing = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    firstName = models.CharField(max_length=40)
    age_at_missing = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=40, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    gender = models.CharField(max_length=1)
    race = models.CharField(max_length=1, null=True, blank=True)

    def __str__(self):
        return self.firstName + " " + self.lastName

    class Meta :
        db_table = "Missing Persons"
