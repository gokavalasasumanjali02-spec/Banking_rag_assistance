from langchain_ollama import OllamaLLM
llm = OllamaLLM(model="llama3")
def ask_llm(question, context):
    prompt = f"""
You are a Banking Assistant.
Context:
{context}
Question:
{question}
Answer:
"""
    return llm.invoke(prompt)