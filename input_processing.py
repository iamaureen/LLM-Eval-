import pandas as pd
import os


def read_questions_from_data(num_questions=20):
    """
    Read questions from the data file in the Data folder.
    
    Args:
        num_questions (int): Number of questions to return (default: 20)
    
    Returns:
        list: List of questions from the 'question' column
    """
    try:
        # Get the path to the Data folder
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_folder = os.path.join(current_dir, 'Data')
        
        # Use the given CSV file name
        csv_file_path = os.path.join(data_folder, "DSL-bio.csv")
        
        # Read the CSV file
        df = pd.read_csv(csv_file_path)
        
        # Check if 'question' column exists
        if 'question' not in df.columns:
            raise ValueError("'question' column not found in the CSV file")
        
        # Get the specified number of questions
        questions = df['question'].head(num_questions).tolist()
        
        print(f"Successfully loaded {len(questions)} questions from DSL-bio.csv")
        return questions
        
    except Exception as e:
        print(f"Error reading questions from data file: {str(e)}")
        return []


def read_full_data(num_questions=20):
    """
    Read the full data from the CSV file including all columns.
    
    Args:
        num_questions (int): Number of rows to return (default: 20)
    
    Returns:
        pandas.DataFrame: DataFrame with all columns from the original data
    """
    try:
        # Get the path to the Data folder
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_folder = os.path.join(current_dir, 'Data')
        
        # Use the given CSV file name
        csv_file_path = os.path.join(data_folder, "DSL-bio.csv")
        
        # Read the CSV file
        df = pd.read_csv(csv_file_path)
        
        # Check if 'question' column exists
        if 'question' not in df.columns:
            raise ValueError("'question' column not found in the CSV file")
        
        # Get the specified number of rows
        df_subset = df.head(num_questions).copy()
        
        print(f"Successfully loaded {len(df_subset)} rows with {len(df_subset.columns)} columns from DSL-bio.csv")
        print(f"Columns: {list(df_subset.columns)}")
        
        return df_subset
        
    except Exception as e:
        print(f"Error reading full data from file: {str(e)}")
        return pd.DataFrame()


if __name__ == "__main__":
    # Test the function
    questions = read_questions_from_data(20)
    print(f"\nFirst 5 questions:")
    for i, question in enumerate(questions[:5], 1):
        print(f"{i}. {question}")