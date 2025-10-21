from config import TEST_LLMs_API_ACCESS_TOKEN, TEST_LLMs_REST_API_URL
from input_processing import read_full_data
from model_processing import process_dataframe_with_models, create_model_configs
from results_handler import save_results_to_excel, print_evaluation_summary


if __name__ == '__main__':
    # Load 20 rows with all columns from the data file
    df = read_full_data(2)
    
    if df.empty:
        print("No data loaded. Exiting.")
        exit(1)
    
    print(f"Loaded {len(df)} rows with {len(df.columns)} columns for LLM evaluation")

    # Create model configurations
    base_model, rag_model = create_model_configs(
        TEST_LLMs_API_ACCESS_TOKEN, 
        TEST_LLMs_REST_API_URL
    )

    # Process all rows with both models
    print("\n" + "="*60)
    print("STARTING LLM EVALUATION")
    print("="*60)
    
    results_df = process_dataframe_with_models(df, base_model, rag_model)
    
    # Save results to Excel file
    print("\n" + "="*60)
    print("SAVING RESULTS")
    print("="*60)
    
    output_file = save_results_to_excel(results_df, "llm_evaluation_results.xlsx")
    
    # Print evaluation summary
    print_evaluation_summary(results_df, output_file)
