from pathlib import Path

def load_documents(data_dir: str):
    docs = []
    for path in Path(data_dir).glob("*.txt"):
        with open(path, "r", encoding="utf-8") as f:
            docs.append(
                {
                    "source": path.name,
                    "text": f.read()
                }
            )
    return docs
