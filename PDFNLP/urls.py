from django.urls import path
from .views import PDFExtractView

app_name = "PDFNLP"

urlpatterns = [path("upload/", PDFExtractView.as_view(), name="upload-pdf")]
