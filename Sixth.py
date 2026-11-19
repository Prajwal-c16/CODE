#import the ollama llm model
import ollama
#assign the role and content to tell that ai
message=[
  {
    #act as a system role (its an llm model direct assigned role.
    "role":"system",
    "content":"act as a bus conductor"
  }
  {
     #its an user role that user tells what to do
    "role":"user",
    "content":"how much price between the shivamogga and bhadravathi busstand"
  }
