from loaders.loader import loader
from chunking.chunker import chunker
from embedding.embedder import Embedder
from retrieval.retreiver import Retriever
from llm.llm import LLM
from prompts.prompt_builder import prompt_builder


class RAGPipeline:

    def __init__(self):

        # classes (stateful)
        self.embedder = Embedder()
        self.retriever = Retriever()
        self.llm = LLM()

        
        docs = loader()              
        chunks = chunker(docs)     

        self.embedded_chunks = self.embedder.embed_chunks(chunks)

    def run(self, query: str):

        query_vector = self.embedder.embedd_query(query)

        retrieved = self.retriever.retrieve(
            query_vector,
            self.embedded_chunks
        )

        prompt = prompt_builder(query, retrieved)

        return self.llm.generate(prompt)
    
# query="what is passive cooling?"
# rag = RAGPipeline()
# answer = rag.run(query)
# print(answer)