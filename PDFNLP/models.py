from django.db import models


class ExtractedData(models.Model):
    username = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    pdf_file = models.FileField(upload_to="pdfs/", null=False, blank=False)
    nouns = models.TextField()
    verbs = models.TextField()

    def __str__(self):
        return self.email
