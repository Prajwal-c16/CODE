import ollama 

model_1="llama3.2latest"

r2=ollama.generate(model=model_1,prompt="Explain system design in one world ")

print(r2.response)
