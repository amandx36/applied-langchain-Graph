# Retriever Semantic Search (LangChain)

This project demonstrates basic semantic search using LangChain.

## Concepts Covered
- Text embeddings using Ollama (`nomic-embed-text`)
- In-memory vector storage
- Retrieval using `as_retriever()`
- Accessing `Document` objects (`page_content`, `id`)

## How it Works
1. Input texts are converted into vector embeddings
2. Stored in an in-memory vector store
3. A query is converted into a vector
4. Similarity search retrieves the closest matching document

## Example
**Query:**  
`How I become a Critical Thinker ?`

**Output:**  
Returns the most semantically similar text from the dataset

## Key Learning
- `retriever.invoke()` returns `List[Document]`
- Access results using:
  ```python
  results[0].page_content
