from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
   api_key = os.getenv("OPENAI_API_KEY"),
)

# upload training file
upload_response = client.files.create(
  file=open("data/data.jsonl", "rb"),
  purpose="fine-tune"
)

# finetune
finetune_response = client.fine_tuning.jobs.create(
  training_file=upload_response.id, 
  model="gpt-3.5-turbo",
  suffix="customized"  #a suffix to create a distinct model name
)

# save the finetuned model ID to 'model_id.txt'
with open('model_id.txt', 'w') as file:
    file.write(finetune_response.id)
