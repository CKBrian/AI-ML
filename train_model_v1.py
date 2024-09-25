#!/usr/bin/env python3
'''Open AI experimental module'''
from dotenv import load_dotenv
import openai
import os

# Get OpenAi api key
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
print(api_key)
openai.api_key(api_key)

# test the model
openai.OpenAI.client = OpenAI()

# Load your CSV file into a pandas DataFrame
df = pd.read_csv('blog_posts_data.csv')
df.head()

#Helper function: get embeddings for a text
def get_embeddings(text):
   response = openai.Embedding.create(
       model="text-embedding-ada-002",
       input = text.replace("\n"," ")
   )
   embedding = response['data'][0]['embedding']
   return embedding

# Tessell for PostgreSQL database connection string
# Found under Tessell Overview tab in Tessell console.
import os
connection_string  = os.environ['TESSELL_POSTGRESQL']
