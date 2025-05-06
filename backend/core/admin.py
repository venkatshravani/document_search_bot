from django.contrib import admin
from .models import Document

# Define a custom admin action to process selected documents
def process_selected_documents(modeladmin, request, queryset):
    for document in queryset:
        # Process documents (e.g., parse files or perform other actions)
        document.parse_file()  # Example: Parse text content from uploaded file
        document.save()

process_selected_documents.short_description = "Process selected documents"

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    # Display fields in the list view
    list_display = ('title', 'uploaded_at', 'user', 'text_content')  # Adding text_content for visibility (optional)
    
    # Search functionality in the admin
    search_fields = ('title', 'user__username')  # Allow searching by title and username
    
    # Filtering options in the list view
    list_filter = ('uploaded_at', 'user')  # Filter by upload date and user
    
    # Make certain fields read-only (e.g., text_content)
    readonly_fields = ('text_content',)  # Make the 'text_content' field read-only
    
    # Add custom admin actions (e.g., to process documents in bulk)
    actions = [process_selected_documents]
    
    # Optionally, you can add more configurations such as form customization, etc.

