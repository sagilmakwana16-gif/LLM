import os
from pathlib import Path
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Load all text files from the data folder
data_folder = Path(__file__).resolve().parent

print("Data folder:", data_folder)
print("Files found:", list(data_folder.glob("*.txt")) + list(data_folder.glob("*.md")))

documents = SimpleDirectoryReader(
    input_dir=str(data_folder),
    required_exts=[".txt", ".md"]
).load_data()

print("Total documents loaded:", len(documents))

# Gemini LLM
llm = GoogleGenAI(
    model="gemini-3.5-flash",
    api_key=api_key
)

# Embedding model
embed_model = GoogleGenAIEmbedding(
    model_name="gemini-embedding-001",
    api_key=api_key
)

# Create index
index = VectorStoreIndex.from_documents(
    documents,
    embed_model=embed_model
)

# Create query engine
query_engine = index.as_query_engine(
    llm=llm,
    similarity_top_k=3
)

# Ask questions
while True:
    question = input("Enter your question: ").strip()

    if question.lower() == "exit":
        break

    if not question:
        continue

    response = query_engine.query(question)
    print("Answer:", response)

