import ollama

message=[
  {
    "role":"system",
    "content":"act as a senior enginner."
  },
  {
    "role":"user",
    "content":"help me build a logical program using java script."
}
]

a=ollama.chat(model="llama3.2:latest",messages=message)
print(a.message)
    
