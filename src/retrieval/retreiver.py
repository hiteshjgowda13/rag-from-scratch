import numpy as np
from chunking.chunking import Chunk
from embedding.embedding import EmbeddedChunk
class Retriever:
    def cosine_similarity(self,query_vector: np.ndarray, chunk_vector:np.ndarray) -> float:
        dot_product = np.dot(query_vector,chunk_vector)
        mag_query = np.linalg.norm(query_vector)
        mag_chunk = np.linalg.norm(chunk_vector)

        cos_sim = dot_product/(mag_chunk*mag_query)

        return cos_sim
    
    def retrieve(self,query_vector:np.ndarray, embedded_chunks:list[EmbeddedChunk], top_k:int =3)->list[tuple]:
        score_list =[]
        
        for vector in embedded_chunks:
            score = self.cosine_similarity(query_vector,vector.embedding)
            score_list.append((vector.chunk,score))

        score_list.sort(reverse=True,key=lambda x:x[1])

        result =score_list[:top_k]

        # for i in range(top_k):
        #     result.append(score_list[i])
        
        print(f"For given query {len(result)} chunks are retrived and returned")

        return result
    


        