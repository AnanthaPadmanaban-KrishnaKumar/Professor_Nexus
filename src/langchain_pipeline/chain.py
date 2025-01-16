from models import query_bedrock

def run_chain(prompt, model_id="gpt-3.5", temperature=0.7, max_tokens=200):
    """
    Runs the chatbot's LangChain pipeline with Bedrock as the LLM backend.
    """
    try:
        response = query_bedrock(model_id, prompt, temperature, max_tokens)
        return response
    except Exception as e:
        return f"An error occurred: {e}"
