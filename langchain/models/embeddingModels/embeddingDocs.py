from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001", 
    dimensions =4
)

documents=[
    "Kathmandu is the captial of Nepal",
    "London is the capital of England",
    "Bangkok is the capital of Thailand"
]

result = embeddings.embed_documents(documents)
print(str(result))
