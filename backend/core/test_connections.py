import openai
from django.conf import settings
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

def test_azure_search():
    try:
        search_client = SearchClient(
            endpoint=settings.AZURE_SEARCH_ENDPOINT,
            index_name=settings.AZURE_SEARCH_INDEX_NAME,
            credential=AzureKeyCredential(settings.AZURE_SEARCH_API_KEY)
        )
        results = search_client.search("*", top=1)  # Search with wildcard to fetch any document
        print("✅ Azure Cognitive Search connection successful.")
        for result in results:
            print(f"Sample document found: {result}")
            break
    except Exception as e:
        print("❌ Azure Cognitive Search connection failed:", e)

def test_openai_api():
    try:
        openai.api_key = settings.OPENAI_API_KEY
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello!"}
            ],
            max_tokens=50
        )
        print("✅ OpenAI GPT-4 connection successful.")
        print("Response:", response.choices[0].message['content'].strip())
    except Exception as e:
        print("❌ OpenAI GPT-4 connection failed:", e)

def run_all_tests():
    print("Running connection tests...\n")
    test_azure_search()
    print("\n")
    test_openai_api()

