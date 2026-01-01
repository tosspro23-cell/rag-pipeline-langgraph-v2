# LangGraph Helper Agent – Heavy RAG Pipeline (v2.1)

> **Production-oriented Retrieval Pipeline for LangGraph & LangChain Documentation**  
> Focused on **context quality, retrieval robustness, and evaluation**, not chatbot UX.

---

## 1. Project Overview

This repository contains **RAG v2.1**, a **Heavy Retrieval-Augmented Generation (RAG) pipeline** designed as a **standalone, production-grade retrieval system**.

Unlike typical end-to-end “RAG chatbots”, this project intentionally **decouples retrieval from generation**, treating retrieval as a **first-class, testable, and evolvable data pipeline**.

### Key goals:
- Demonstrate **engineering-grade RAG design**
- Emphasize **retrieval quality over LLM fluency**
- Enable **debuggability, evaluation, and iteration**
- Serve as a **drop-in retrieval backend** for agent systems (e.g. LangGraph Helper Agent v1)

---

## 2. Design Philosophy

### Why “Heavy RAG”?

In real-world systems, most failures attributed to “LLMs” are actually caused by:
- Poor chunking
- Low-quality embeddings
- Inadequate retrieval
- Unobservable context assembly

This project focuses on **solving the hard part**:

> **“What context should the model see — and why?”**

### Explicit trade-offs:
- ✅ Determinism over emergent behavior  
- ✅ Observability over hidden prompt magic  
- ✅ Retrieval correctness over conversational smoothness  

---

## 3. Architecture Overview

```
┌────────────┐
│  Raw Docs  │
│ (llms.txt) │
└─────┬──────┘
      │
      ▼
┌────────────┐
│  Loader    │
└─────┬──────┘
      │
      ▼
┌────────────┐
│  Chunker   │
└─────┬──────┘
      │
      ▼
┌────────────┐
│ Embedder   │
└─────┬──────┘
      │
      ▼
┌────────────┐
│ Vector DB  │
│ (Chroma)   │
└─────┬──────┘
      │
      ▼
┌────────────┐
│ Retriever  │
└─────┬──────┘
      │
      ▼
┌────────────┐
│ Evaluation │
└────────────┘
```

---

## 4. Repository Structure

```
.
├── data/
│   ├── langgraph_llms.txt
│   └── langchain_llms.txt
│
├── rag/
│   ├── loader.py
│   ├── chunker.py
│   ├── embedder.py
│   ├── vectorstore.py
│   ├── retriever.py
│
├── eval/
│   ├── debug.py
│   └── metrics.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 5. Data Sources (Offline, Deterministic)

- LangGraph official documentation (llms.txt)
- LangChain official documentation (llms.txt)

### Update strategy:
- Manual update via GitHub commit
- Clear diff visibility
- Optional automation hook (future work)

---

## 6. Chunking Strategy (v2.1)

- Semantic-aware fixed-size chunking
- Configurable chunk size and overlap
- Strategy isolated for easy replacement

---

## 7. Embedding Layer

- Abstracted embedding interface
- Backend-agnostic
- Designed for controlled experiments

---

## 8. Vector Store

- Chroma (local, inspectable)
- Zero external dependencies
- Developer-friendly debugging

---

## 9. Retrieval Layer

- Query embedding
- Similarity search
- Top-K context selection

Retrieval output is **inspectable before LLM usage**.

---

## 10. Evaluation & Debugging

- Debug mode for retrieved chunks
- Coverage and redundancy inspection
- Failure case analysis
- LLM-independent evaluation

---

## 11. Why This Is Not a Chatbot

This project does **not** optimize for:
- Conversational UX
- Prompt tricks
- End-to-end answer generation

It optimizes for **retrieval correctness**.

---

## 12. Relationship to LangGraph Helper Agent (v1)

- Acts as a drop-in retrieval backend
- Complements agent orchestration
- Enables production-grade context engineering

---

## 13. Roadmap

- Re-ranking
- Hybrid retrieval
- Automated metrics
- Regression tests
- Online ingestion

---

## 14. Summary

This project demonstrates:
- Production-grade RAG thinking
- Pipeline-oriented design
- Deterministic retrieval
- Clear separation of concerns

---

**Author:** Ting Li  
AI Systems · Agent Architecture · RAG Engineering
