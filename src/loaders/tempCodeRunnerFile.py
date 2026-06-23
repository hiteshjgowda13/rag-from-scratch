from pathlib import Path
from document import Document
def loader():
    folder = Path("data/raw")
    documents_list :list[Document]=[]
    
    for file in folder.glob("*.txt"):
        print(file)