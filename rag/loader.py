from pathlib import Path

def load_documents(data_dir: str):
    docs = []
    data_path = Path(data_dir)

    print(f"[DEBUG] Loading documents from: {data_path.resolve()}")

    if not data_path.exists():
        print(f"[ERROR] Data directory does not exist: {data_path}")
        return []

    paths = list(data_path.glob("*.txt"))
    print(f"[DEBUG] Found {len(paths)} .txt files")

    for path in paths:
        print(f"[DEBUG] Loading file: {path.name}")
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
            print(f"[DEBUG] {path.name} length: {len(text)} chars")
            docs.append(
                {
                    "source": path.name,
                    "text": text
                }
            )

    print(f"[DEBUG] Total loaded documents: {len(docs)}")
    return docs
