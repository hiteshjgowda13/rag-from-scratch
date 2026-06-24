from fastapi import FastAPI
from pydantic import BaseModel

from rag.pipeline import RAGPipeline

app = FastAPI(title="RAG From Scratch", version="1.0")

# initialize pipeline ONCE (important) as it loades the hugging face model chunks and loads documents aste
rag = RAGPipeline()

class QueryRequest(BaseModel):
    question: str


class QueryResponse(BaseModel):
    answer: str

@app.post("/query", response_model=QueryResponse)
def query(req: QueryRequest):

    answer = rag.run(req.question)

    return QueryResponse(answer=answer)