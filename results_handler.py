import pandas as pd
import os
from openpyxl.styles import Alignment


def save_results_to_excel(results, output_filename="llm_evaluation_results.xlsx"):
    """
    Save the results to an Excel file with proper formatting in the Output folder.
    
    Args:
        results (pandas.DataFrame or list): DataFrame with results or list of result dictionaries
        output_filename (str): Name of the output Excel file
    
    Returns:
        str or None: Path to saved file if successful, None if failed
    """
    try:
        # Handle both DataFrame and list inputs
        if isinstance(results, pd.DataFrame):
            df = results.copy()
        else:
            # Create DataFrame from list of dictionaries
            df = pd.DataFrame(results)
            # Reorder columns for better readability if it's a list
            if 'question_id' in df.columns:
                df = df[['question_id', 'question', 'base_model_response', 'rag_model_response']]
        
        # Get the current directory and create Output folder
        current_dir = os.path.dirname(os.path.abspath(__file__))
        output_folder = os.path.join(current_dir, 'Output')
        
        # Create Output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)
        
        # Create full output path
        output_path = os.path.join(output_folder, output_filename)
        
        # Save to Excel with formatting
        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='LLM_Evaluation_Results', index=False)
            
            # Get the workbook and worksheet for formatting
            workbook = writer.book
            worksheet = writer.sheets['LLM_Evaluation_Results']
            
            # Adjust column widths dynamically based on content
            for col_idx, column in enumerate(df.columns, 1):
                col_letter = chr(64 + col_idx)  # Convert to Excel column letter
                
                if column in ['qid', 'question_id']:
                    worksheet.column_dimensions[col_letter].width = 10
                elif column == 'question':
                    worksheet.column_dimensions[col_letter].width = 60
                elif 'response' in column.lower():
                    worksheet.column_dimensions[col_letter].width = 80
                else:
                    worksheet.column_dimensions[col_letter].width = 30
            
            # Wrap text for better readability
            for row in worksheet.iter_rows():
                for cell in row:
                    cell.alignment = Alignment(wrap_text=True, vertical='top')
        
        print(f"Results saved to: {output_path}")
        return output_path
        
    except Exception as e:
        print(f"Error saving results to Excel: {str(e)}")
        return None


def print_evaluation_summary(results, output_file):
    """
    Print a summary of the evaluation results.
    
    Args:
        results (pandas.DataFrame or list): DataFrame with results or list of result dictionaries
        output_file (str): Path to the saved Excel file
    """
    if output_file:
        print(f"\n✓ Evaluation completed successfully!")
        print(f"✓ Results saved to: {output_file}")
        
        # Handle both DataFrame and list inputs
        if isinstance(results, pd.DataFrame):
            total_rows = len(results)
            successful_base = sum(1 for r in results['base_model_response'] if not str(r).startswith('ERROR:'))
            successful_rag = sum(1 for r in results['rag_model_response'] if not str(r).startswith('ERROR:'))
        else:
            total_rows = len(results)
            successful_base = sum(1 for r in results if not r['base_model_response'].startswith('ERROR:'))
            successful_rag = sum(1 for r in results if not r['rag_model_response'].startswith('ERROR:'))
        
        print(f"✓ Processed {total_rows} questions with both models")
        print(f"✓ Base model: {successful_base}/{total_rows} successful responses")
        print(f"✓ RAG model: {successful_rag}/{total_rows} successful responses")
    else:
        print(f"\n✗ Error saving results to Excel file")