from ASUllmAPI import ModelConfig, query_llm


def execute_single_query(model_name, user_query):
    """
    Execute a single query against an LLM model.
    
    Args:
        model_name: Model configuration object
        user_query (str): The question/query to send to the model
    
    Returns:
        str: The response from the model
    """
    llm_response = query_llm(model=model_name, query=user_query)
    return llm_response.get('response')


def process_questions_with_models(questions, base_model, rag_model):
    """
    Process all questions with both base model and RAG model.
    
    Args:
        questions (list): List of questions to process
        base_model: Base model configuration
        rag_model: RAG model configuration
    
    Returns:
        list: List of dictionaries containing question and responses from both models
    """
    results = []

    print(f"Processing {len(questions)} questions with both models...")

    for i, question in enumerate(questions, 1):
        print(f"Processing question {i}/{len(questions)}: {question[:50]}...")

        try:
            # Process with base model first
            print(f"  Querying base model...")
            base_response = execute_single_query(base_model, question)

            # Process with RAG model
            print(f"  Querying RAG model...")
            rag_response = execute_single_query(rag_model, question)

            # Store results maintaining order
            result = {
                'question_id': i - 1,  # 0-based index to match original data
                'question': question,
                'base_model_response': base_response,
                'rag_model_response': rag_response
            }
            results.append(result)

            print(f"  ✓ Completed question {i}")

        except Exception as e:
            print(f"  ✗ Error processing question {i}: {str(e)}")
            # Add error result to maintain order
            result = {
                'question_id': i - 1,
                'question': question,
                'base_model_response': f"ERROR: {str(e)}",
                'rag_model_response': f"ERROR: {str(e)}"
            }
            results.append(result)

    return results


def process_dataframe_with_models(df, base_model, rag_model):
    """
    Process a DataFrame with both base model and RAG model, preserving all original columns.
    
    Args:
        df (pandas.DataFrame): DataFrame containing the data to process
        base_model: Base model configuration
        rag_model: RAG model configuration
    
    Returns:
        pandas.DataFrame: DataFrame with original columns plus LLM responses
    """
    results_df = df.copy()
    
    print(f"Processing {len(df)} rows with both models...")
    
    base_responses = []
    rag_responses = []
    
    for i, row in df.iterrows():
        question = row['question']
        print(f"Processing row {i+1}/{len(df)}: {question[:50]}...")
        
        try:
            # Process with base model first
            print(f"  Querying base model...")
            base_response = execute_single_query(base_model, question)
            
            # Process with RAG model
            print(f"  Querying RAG model...")
            rag_response = execute_single_query(rag_model, question)
            
            base_responses.append(base_response)
            rag_responses.append(rag_response)
            
            print(f"  ✓ Completed row {i+1}")
            
        except Exception as e:
            print(f"  ✗ Error processing row {i+1}: {str(e)}")
            # Add error responses to maintain order
            base_responses.append(f"ERROR: {str(e)}")
            rag_responses.append(f"ERROR: {str(e)}")
    
    # Add the LLM responses as new columns
    results_df['base_model_response'] = base_responses
    results_df['rag_model_response'] = rag_responses
    
    return results_df


def create_model_configs(access_token, api_url):
    """
    Create model configurations for base and RAG models.
    
    Args:
        access_token (str): API access token
        api_url (str): API URL
    
    Returns:
        tuple: (base_model, rag_model) configuration objects
    """
    # Define the base model
    base_model = ModelConfig(
        name="gpt4o",
        provider="openai",
        access_token=access_token,
        api_url=api_url
    )

    # Define the RAG model
    rag_model = ModelConfig(
        project_id="bfe0772659f1497787895fbb5d1eb622",
        access_token=access_token,
        api_url=api_url,
        enable_history=None,
        enable_search=None,
        search_db_type=None,
        search_collection=None,
        search_retrieval_type=None,
        search_prompt_mode=None,
        rerank=None
    )

    return base_model, rag_model
