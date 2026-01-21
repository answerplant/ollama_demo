import ollama

ollama.embed(
  model='nomic-embed-text',
  input='Llamas are members of the camelid family',
)