from dataclasses import dataclass
from typing import Any
@dataclass
class Document:
    page_content: str
    metadata: dict[str,Any] #keys is str and value can be any

# my_doc = Document(
#     page_content="hello",
#     metadata={
#         "author":"hi",
#         "page":1
#     }
# )
# print(my_doc)