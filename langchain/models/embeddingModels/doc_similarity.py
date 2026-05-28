from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(
    model= "models/embedding-001"
)
sentences = [
    "Lionel Messi is known for his incredible dribbling and playmaking skills.",
    "Cristiano Ronaldo has scored over 800 career goals across club and country.",
    "Neymar Jr. is a Brazilian forward famous for his flair and creativity on the ball.",
    "Kylian Mbappé won the World Cup with France at just 19 years old.",
    "Kevin De Bruyne is widely regarded as one of the best midfielders in the world."
]

query= "who is a midfielder?"

doc_embeddings= embedding.embed_documents(sentences)
query_embeddings= embedding.embed_query(query)


sources=cosine_similarity([query_embeddings],doc_embeddings)[0]

index, source= sorted(list(enumerate(sources)), key= lambda x:x[1])[-1]