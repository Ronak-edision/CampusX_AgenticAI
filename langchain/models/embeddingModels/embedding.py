import logging
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_cohere import CohereEmbeddings
import logging
from dotenv import load_dotenv

load_dotenv()

# embeddings = GoogleGenerativeAIEmbeddings(
#     model="models/embedding-001", 
#     dimensions =4
# )

logging.getLogger("sagemaker.config").setLevel(logging.WARNING)
embeddings = CohereEmbeddings(
    model="embed-english-light-v3.0",  
)
result = embeddings.embed_query("Hello, world!")
print(result)
print(f"Embedding dimension: {len(result)}")
