from chunking.chunking import Chunk

def prompt_builder(query:str,contents:list[tuple])->str:
    meta_data =[]
    context_string =""
    for i in range(len(contents)):
        chunk = contents[i][0]
        context_string = context_string + "  " + chunk.content
        meta_data.append(chunk.metadata["source"])
    
    answer = f"your an helpfull assistant \nuse ONLY the provided context for generating an answer for the question\nif answer is not present in context, say:\n'I couldnt find answer in the documents' : \n\t context: {context_string} \n\t source: {meta_data} \n\t question: {query} \n\t generate an answer for this \n\t answer:"

    return answer

# testing
# query="what is passive cooling?"
# chunk1 = Chunk(
#     content="passive cooling is nothing but ",
#     metadata={
#         "source":"me"
#     }
# )
# chunk2 = Chunk(
#     content="passive cooling always works for me not for others",
#     metadata={
#         "source":"m2"
#     }
# )
# contents=[(chunk1,0.93),(chunk2,0.88)]

# result = prompt_builder(query,contents)
# print(result)