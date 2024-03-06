import pandas as pd
import os

def create_text_files(csv_file, output_dir):
    # Read the CSV file
    data = pd.read_csv(csv_file, sep='|', header=0, names=['Text', 'Label'])

    # Iterate over each row
    for index, row in data.iterrows():
        class_folder = os.path.join(output_dir, str(row['Label']))
        os.makedirs(class_folder, exist_ok=True)
        file_path = os.path.join(class_folder, f'text{index}.txt')
        
        # Convert the text to a string and write to a file
        text_str = str(row['Text'])
        with open(file_path, 'w') as file:
            file.write(text_str)

# Paths to your CSV files
dev_csv = 'OGtriage/dev.csv'
train_csv = 'OGtriage/train.csv'

# Create text files for each dataset
create_text_files(train_csv, 'train')
create_text_files(dev_csv, 'dev')
