from pathlib import Path
from document import Document
def loader():

    folder = Path("data/raw")
    documents_list :list[Document]=[]
    count =1
    if folder.exists():
        for file in folder.glob("*.txt"):
            # print(file.read_text(encoding="utf-8")[:100])
            # print(file.name+ " complete")
            file_content = file.read_text(encoding="utf-8")
            metadata_content ={
                "source":file.name,
                "file_type":".txt",
                "doc_id":count,
                "size_bytes": file.stat().st_size
            }
            count +=1
            doc =Document(
                page_content=file_content,
                metadata=metadata_content
            )
            documents_list.append(doc)
    else:
        print("no such path")

    return documents_list

# print(loader())

