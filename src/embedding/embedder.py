from embedding.embedding import EmbeddedChunk
from chunking.chunking import Chunk
from sentence_transformers import SentenceTransformer

class Embedder:
    """
    class to generate vector embedding for given query or from chunks
    """

    def __init__(self,model_name:str= "all-MiniLM-L6-v2"):
        """to initialize the model """

        print("Initialzing the model ")

        self.model = SentenceTransformer(model_name)
        print("model initilization complete")

        # this make sures tht model loads once not evrytime
    
    def embed_chunks(self,chunks:list[Chunk])->list[EmbeddedChunk]:
        """ to embedd the chunks """
        embeddings=[]

        if not chunks:
            return []
        
        text =[
            chunk.content for chunk in chunks
        ]
        
        text_to_vector = self.model.encode(text,convert_to_numpy=True)

        for i in range(len(chunks)):
            embed = EmbeddedChunk(
                chunk=chunks[i],
                embedding=text_to_vector[i]
            )
            embeddings.append(embed)
    
        return embeddings
            

#testing: works 
# chunks = [
#     Chunk(
#         content="hi hello how are you?",
#         metadata={
#             "source":"me",
#             "chunk_id":1
#         }
#     ),
#     Chunk(
#         content="Nice to meet u hope u had good",
#         metadata={
#             "source":"me",
#             "chunk_id":2
#         }
#     )
# ]
# embedder = Embedder()

# embedded_chunks =embedder.embed_chunks(chunks)

# # print(type(embedded_chunks))
# # print(len(embedded_chunks))
# print(embedded_chunks[0])
# print(embedded_chunks[0].chunk.content)
# print(embedded_chunks[0].chunk.metadata)
# print(embedded_chunks[0].embedding.shape)