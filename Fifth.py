import ollama

message=[
  {
    "role":"system",
    "content":"Act like an frend to learn new topics"
  }
  {
    "role":"user",
    "content":"help me to build an e commerce website for my business"
  }
]
model_name:llama3.2:latest
R=ollama.chat=(model=model_name,messages=message)
print(R.message)
