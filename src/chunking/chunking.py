# chunking means to divide huge docs into smaller part 
# with chunk size and overlap
# overlap is neccessary for not forgettihng more smtng like tht

# if we dont chunk
# -embedding becomes noisy
# -retrievel becomes irrellvant
# -llm gets to much context
# -cost increases (token)
# -accuracy drops


from dataclasses import dataclass

@dataclass
class Chunk:
    content:str
    metadata:dict
    