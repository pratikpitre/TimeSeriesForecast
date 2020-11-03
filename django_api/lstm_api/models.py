from django.db import models

# Create your models here.
class Predict(models.Model):
    input_seqone = models.IntegerField()
    input_seqtwo = models.IntegerField()
    input_seqthree = models.IntegerField()

    def __str__(self):
        return self.input_seqone, self.input_seqtwo, self.input_seqthree
