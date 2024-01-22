## steps to run the project
''' bash

conda create -n IE python=3.8 -y

conda activate IE

pip install -r requirements.txt

'''
### create a '.env' file in the root directory and add your pinecone credentials as follows:

''' ini
PINECONE_API_KEY = your_api_key
PINECONE_API_ENV = your _api_env
'''
### Download the quantize model from the link provided in model folder & keep the model in the model directory:

''' ini
## Download th Llama 2 model:

llama-2-7b-chat.ggmlv3.q4_0.bin

## from the following link:

https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main

'''