from django.db import models

class University(models.Model):
    UniversityIndex = models.AutoField(primary_key=True, default=None)
    UniversityName = models.CharField(max_length=255)
    GREscore = models.IntegerField(default=0)
    GPA = models.FloatField(default=0.0)
    IELTSscore = models.FloatField(default=0.0)
    ResearchPaper = models.IntegerField(default=0)
    UniversityRanking = models.IntegerField(default=0)
    AdmitProbability = models.FloatField(default=0.0)
    country = models.CharField(max_length=50, default='US')
    course = models.CharField(max_length=255, default='CS/CE')

    def __str__(self):
        return self.UniversityName
