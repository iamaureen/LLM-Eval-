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


if __name__ == "__main__":
    # Test the function
    questions = read_questions_from_data(20)
    print(f"\nFirst 5 questions:")
    for i, question in enumerate(questions[:5], 1):
        print(f"{i}. {question}")