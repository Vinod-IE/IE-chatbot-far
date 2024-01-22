prompt_template = """
Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know; don't try to make up an answer.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""

# Example usage:
context = "I am seeking accurate information from the Federal Acquisition Regulation (FAR) pdf."
question = "What are the key provisions related to procurement processes in the FAR?"

full_prompt = prompt_template.format(context=context, question=question)
print(full_prompt)
