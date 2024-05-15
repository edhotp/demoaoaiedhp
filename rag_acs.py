import os
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

endpoint = ""
deployment = "gpt-4-turbo"
search_endpoint = ""
search_index = ""

token = ""

client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=token,
    api_version="2024-02-01",
)

completion = client.chat.completions.create(
    model=deployment,
    messages=[
        {
		"role": "system",
		"content": "You are an AI assistant that helps people find information."
	    },
	    {
		    "role": "user",
		    "content": "jelaskan secara singkat tentang sustainability di biofarma"
	    },
    ],
    extra_body={
        "data_sources": [
            {
                "type": "azure_search",
                "parameters": {
                    "endpoint": search_endpoint,
                    "index_name": search_index,
                    "strictness": 3,
                    "top_n_documents": 5,
                    "query_type": "vector_simple_hybrid",
                    "embedding_dependency": {
                        "type": "deployment_name",
                        "deployment_name": "text-embedding-ada-002"
                    },
                    "authentication": {
                        "type": "api_key",
                        "key": ""
                    }
                }
            }
        ]
    }
)

print(completion.model_dump_json(indent=2))