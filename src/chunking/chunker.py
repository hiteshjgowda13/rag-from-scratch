from chunking.chunking import Chunk
from loaders.document import Document

def chunker(docs:list[Document], chunk_size: int = 300, chunk_overlap: int  = 100) -> list[Chunk]:

    chunks = []
    chunk_count = 1

    step = chunk_size - chunk_overlap
    if step <= 0:
        raise ValueError("chunk_size must be greater than chunk_overlap")
    
    for doc in docs:
        words = doc.page_content.split()

        for i in range(0,len(words),step):
            word_slice = words[i:chunk_size+i]
            content = " ".join(word_slice)
            chunk = Chunk(
                content=content,
                metadata={
                    "source":doc.metadata["source"],
                    "from_doc":doc.metadata["doc_id"],
                    "chunk_id":chunk_count
                }
            )

            chunks.append(chunk)
            chunk_count +=1
    print(f"for {len(docs)} documents given {chunk_count} is created")
    return chunks

# testing
# doc=Document(
#     page_content="hello i am amazingly fine how are u this is a test to check my chunking function hope it works!!!",
#     metadata={
#         "source":"myself",
#         "doc_id":1
#     }
# )
# docs=[]
# docs.append(doc)

# answer = chunker(docs,4,2)
# print(answer)