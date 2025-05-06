import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets, status
from django.core.files.storage import default_storage
from rest_framework.decorators import api_view

from .models import Document
from .serializers import DocumentSerializer
from utils.file_utils import extract_text_from_pdf, chunk_text, save_file
from utils.openai_utils import get_embedding_with_cache

# Upload API
class DocumentUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file = request.FILES['file']
        document = Document.objects.create(file=file)
        serializer = DocumentSerializer(document)
        return Response({'message': 'File uploaded successfully', 'data': serializer.data})

        try:
            # Save file
            absolute_file_path = save_file(file_obj, default_storage)

            # Extract and chunk text
            extracted_text = extract_text_from_pdf(absolute_file_path)
            document_id = os.path.splitext(file_obj.name)[0]
            chunks = chunk_text(extracted_text)

            # Create embeddings and (placeholder for indexing)
            for i, chunk in enumerate(chunks):
                embedding = get_embedding_with_cache(chunk, f"{document_id}_chunk_{i}")
                # TODO: Push to Azure Cognitive Search

            # Save document to DB
            Document.objects.create(
                title=title,
                file=file_obj,
                user=request.user,
                text_content=extracted_text
            )

            return Response({"message": "Uploaded and indexed successfully"}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# ViewSet for document listing
class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

# Search API
@api_view(['GET'])
def search_documents(request):
    query = request.GET.get('q', '')
    if not query:
        return Response({"error": "Query parameter `q` is required."}, status=400)

    # Placeholder: In production, use Azure Cognitive Search or vector DB
    matching_docs = Document.objects.filter(text_content__icontains=query)
    serializer = DocumentSerializer(matching_docs, many=True)
    return Response(serializer.data)
