import os
import shutil

def collect_and_rename_files(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    for root, dirs, files in os.walk(input_directory):
        for file in files:
            parent_dir = os.path.basename(root)
            new_file_name = f"{parent_dir}_{file}"
            full_file_path = os.path.join(root, file)
            new_file_path = os.path.join(output_directory, new_file_name)
            shutil.copy2(full_file_path, new_file_path)

if __name__ == "__main__":
    input_directory = "/Users/cyixiao/Desktop/llm/DATA/text"
    output_directory = "/Users/cyixiao/Desktop/llm/DATA/zhwiki_text"
    collect_and_rename_files(input_directory, output_directory)
