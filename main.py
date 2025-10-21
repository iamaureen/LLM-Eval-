from config import TEST_LLMs_API_ACCESS_TOKEN, TEST_LLMs_REST_API_URL
from ASUllmAPI import ModelConfig, query_llm


def execute_single_query(model_name, user_query):
    # Use query_llm module to query ASU GPT.
    llm_response = query_llm(model=model_name,
                             query=user_query)
    return llm_response.get('response')


if __name__ == '__main__':
    # define the model
    rag_model = ModelConfig(project_id="bfe0772659f1497787895fbb5d1eb622",
                        access_token=TEST_LLMs_API_ACCESS_TOKEN,
                        api_url=TEST_LLMs_REST_API_URL,
                        enable_history=None,
                        enable_search=None,
                        search_db_type = None,
                        search_collection=None,
                        search_retrieval_type= None,
                        search_prompt_mode= None,
                        rerank=None)


    query = "How many assignments are there?"
    response_text = execute_single_query(rag_model, query)

    print(response_text)
