import dspy
import os
from dotenv import load_dotenv
load_dotenv()

# Set your Groq API key (replace "<your_groq_api_key>" if not using environment variables)
api_key = os.environ.get("OPENAI_API_KEY")

# 1. Configure DSPy to use the Groq language model
# Using 'llama3-8b-8192' as an example model
lm = dspy.LM('ollama_chat/llama3.2:1b', api_base='http://localhost:11434')
dspy.configure(lm=lm, allow_tool_async_sync_conversion=True)



def search_wikipedia(query: str) -> list[str]:
    results = dspy.ColBERTv2(url="https://en.wikipedia.org/wiki/AI_agent")(query, k=3)
    return [x["text"] for x in results]

rag = dspy.ChainOfThought("context, question -> response")

question = "What's the history of AI?"
rag(context=search_wikipedia(question), question=question)
print(rag.response)