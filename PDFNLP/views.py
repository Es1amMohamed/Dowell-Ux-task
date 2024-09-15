import spacy
import PyPDF2
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ExtractedData
from .serializers import ExtractedDataSerializer

nlp = spacy.load("en_core_web_sm")


class PDFExtractView(APIView):
    """
    API View to handle PDF file uploads, extract text from the PDF,
    identify nouns and verbs from the extracted text using spaCy,
    and save the extracted data to the database.

    Methods
    -------
    post(request):
        Handles POST requests to upload a PDF file, extract nouns and verbs,
        and save the data to the database.
    """

    def post(self, request):
        """
        Handle POST requests to process the uploaded PDF file.

        Parameters
        ----------
        request : rest_framework.request.Request
            The request object containing the PDF file and additional data.

        Returns
        -------
        Response
            A response object indicating the success or failure of the operation.
        """

        serializer = ExtractedDataSerializer(data=request.data)

        if serializer.is_valid():
            pdf_file = request.FILES.get("pdf_file")
            if not pdf_file:
                return Response(
                    {"error": "PDF file is required."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            try:

                pdf_reader = PyPDF2.PdfReader(pdf_file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text()

                doc = nlp(text)
                nouns = [token.text for token in doc if token.pos_ == "NOUN"]
                verbs = [token.text for token in doc if token.pos_ == "VERB"]

                extracted_data = ExtractedData(
                    username=request.data.get("username"),
                    email=request.data.get("email"),
                    pdf_file=pdf_file,
                    nouns=", ".join(nouns),
                    verbs=", ".join(verbs),
                )
                extracted_data.save()

                return Response(
                    {"message": "Data extracted and saved successfully."},
                    status=status.HTTP_201_CREATED,
                )

            except Exception as e:
                return Response(
                    {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
