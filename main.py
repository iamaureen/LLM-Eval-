from config import TEST_LLMs_API_ACCESS_TOKEN, TEST_LLMs_REST_API_URL
from ASUllmAPI import ModelConfig, query_llm
from input_processing import read_questions_from_data


def execute_single_query(model_name, user_query):
    # Use query_llm module to query ASU GPT.
    llm_response = query_llm(model=model_name,
                             query=user_query)
    return llm_response.get('response')


if __name__ == '__main__':
    # Load 20 questions from the data file
    questions = read_questions_from_data(20)
    
    if not questions:
        print("No questions loaded. Exiting.")
        exit(1)
    
    print(f"Loaded {len(questions)} questions for LLM evaluation")
    
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

    # Example: Process the first question
    if questions:
        first_question = questions[0]
        print(f"\nProcessing first question: {first_question}")
        response_text = execute_single_query(rag_model, first_question)
        print(f"Response: {response_text}")
