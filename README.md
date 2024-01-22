# Chat with pdf

## Steps to Run the Project

### Step 1: Create a Conda Environment

```bash
conda create -n IE python=3.8 -y
conda activate IE
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```
### Step 3: Set up Pinecone Credentials
Create a '.env' file in the root directory and add your Pinecone credentials as follows:

ini
PINECONE_API_KEY = your_api_key
PINECONE_API_ENV = your_api_env
