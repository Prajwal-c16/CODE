import ollama

model-3="llama3.2:latest"
prompt1="road map for bca student to ace google company with high packages"

r3=ollama.generate(model=model-3,prompt=prompt1
print(r3.response)
