from django.db import models
from django.contrib.auth.models import User  # Import the User model
from .utils import extract_pdf_text, extract_word_text, extract_excel_text, extract_pptx_text

class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_content = models.TextField(blank=True, null=True)  # Store parsed text
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            self.parse_file()

    def parse_file(self):
        """
        Parse the uploaded file based on its extension and extract its text content.
        """
        # Determine the file extension (lowercase for uniformity)
        file_type = self.file.name.split('.')[-1].lower()

        try:
            with open(self.file.path, 'rb') as f:
                # Depending on file type, use the respective extraction function
                if file_type == 'pdf':
                    self.text_content = extract_pdf_text(f)
                elif file_type == 'docx':
                    self.text_content = extract_word_text(f)
                elif file_type == 'xlsx':
                    self.text_content = extract_excel_text(f)
                elif file_type == 'pptx':
                    self.text_content = extract_pptx_text(f)
                else:
                    # Handle unsupported file types
                    self.text_content = "Unsupported file type"
        except Exception as e:
            self.text_content = f"Error parsing file: {str(e)}"

        # Save the parsed text content to the database
        self.save()

    def __str__(self):
        return self.title
