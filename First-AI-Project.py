import ollama 
response=ollama.generate(model=llama3.2:latest,prompt="Explain AI in one line")
print(response.response)
