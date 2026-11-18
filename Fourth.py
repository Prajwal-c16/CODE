import ollama 

model_name="llama3.2:latest "
prompt1="how to connect the frontend and backend with database in a web application and i build website using MERN stack explain in 2-5 simple points  lines in kannada languages."
R=ollama.generate(model=model_name,prompt=prompt1)
print(R.response)