import os
import shutil
import sys

def analyze_data_for_subject(subject_name, condition_n, repetition_m, png_filename):
    """
    Moves the PNG file from the Downloads folder to the appropriate folder on the local machine.

    Args:
        subject_name (str): Name of the subject (e.g., 'vijay').
        condition_n (int): Condition number (e.g., 2).
        repetition_m (int): Repetition number (e.g., 3).
        png_filename (str): Name of the PNG file to be moved (e.g., 'vijay_audio_condition_2_Repetition_3.png').
    """
    # Debug: Print the input arguments
    print(f"Subject Name: {subject_name}")
    print(f"Condition Number: {condition_n}")
    print(f"Repetition Number: {repetition_m}")
    print(f"PNG Filename: {png_filename}")

    # Define the base directory
    base_dir = '/Users/vsingh1/Documents/BackgroundEffect/Data'

    # Construct the folder path
    folder_path = os.path.join(
        base_dir,
        f'{subject_name}_audio',  # e.g., 'vijay_audio'
        f'condition_{condition_n}',  # e.g., 'condition_2'
        f'repetition_{repetition_m}'  # e.g., 'repetition_3'
    )

    # Debug: Print the folder path
    print(f"Destination folder: {folder_path}")

    # Create the folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)

    # Define the full path for the PNG file
    save_path = os.path.join(folder_path, png_filename)

    # Debug: Print the source and destination paths
    print(f"Source file: {png_filename}")
    print(f"Destination file: {save_path}")

    # Move the PNG file to the correct folder
    if os.path.exists(png_filename):
        shutil.move(png_filename, save_path)
        print(f"Plot moved to: {save_path}")
    else:
        print(f"Error: File '{png_filename}' not found in the current directory.")

# Example usage (this part is optional and can be removed if you're calling the function from the terminal)
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python3 analyze_data_for_subject.py <subject_name> <condition_n> <repetition_m> <png_filename>")
    else:
        subject_name = sys.argv[1]
        condition_n = int(sys.argv[2])
        repetition_m = int(sys.argv[3])
        png_filename = sys.argv[4]
        analyze_data_for_subject(subject_name, condition_n, repetition_m, png_filename)