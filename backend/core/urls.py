from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DocumentUploadView, DocumentViewSet, search_documents

# Initialize the router and register the Document viewset
router = DefaultRouter()
router.register(r'documents', DocumentViewSet)

# URL patterns for the core app
urlpatterns = [
    # Endpoint for uploading documents
   path('api/upload/', DocumentUploadView.as_view(), name='upload-document'),
    
    # Endpoint for searching documents
    path('api/search/', search_documents, name='document-search'),
    
    # ViewSet routes (list, retrieve, update, delete)
    path('api/', include(router.urls)),
]






