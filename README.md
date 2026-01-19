Based on the Ollama tutorial for embedding models - https://ollama.com/blog/embedding-models
The initial commit includes minor fixes: the ollama.embed parameter 'input' was set to 'input' instead of 'prompt' and the collection.query parameter 'query_embeddings' was altered to reference the first element of reponse["embeddings"] to retrieve the correct structure.
