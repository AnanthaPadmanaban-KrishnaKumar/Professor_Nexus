import json
from config import get_bedrock_client

def query_bedrock(model_id, prompt, temperature=0.7, max_tokens=200):
    """
    Sends a prompt to an Amazon Bedrock model and retrieves the response.
    """
    client = get_bedrock_client()

    # Bedrock payload
    payload = {
        "inputText": prompt,
        "parameters": {
            "temperature": temperature,
            "maxTokens": max_tokens,
        },
    }

    try:
        # Serialize payload to JSON
        payload_json = json.dumps(payload)

        # Invoke the Bedrock model
        response = client.invoke_model(
            modelId=model_id,
            body=payload_json,  # Pass the serialized JSON payload
            contentType="application/json",
        )

        # Extract and return the response
        response_body = response["body"].read().decode("utf-8")
        return response_body
    except Exception as e:
        raise RuntimeError(f"Error querying Bedrock: {e}")
