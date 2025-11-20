import os
import shutil

def remove_pycache(root_dir):
    for root, dirs, files in os.walk(root_dir):
        if '__pycache__' in dirs:
            shutil.rmtree(os.path.join(root, '__pycache__'))
            dirs.remove('__pycache__')

def save_structure(root_dir, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for item in os.listdir(root_dir):
            item_path = os.path.join(root_dir, item)
            if item == '.git':
                continue
            f.write(f"{item_path}\n")
            if os.path.isdir(item_path):
                save_substructure(item_path, f)
            elif item.endswith(('.tsx', '.ts', '.css')):
                save_content(item_path, f)

def save_substructure(dir_path, output_file):
    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        if os.path.isdir(item_path):
            output_file.write(f"{item_path}\n")
            save_substructure(item_path, output_file)
        elif item.endswith(('.tsx', '.ts', '.css')): # , ".json"
            save_content(item_path, output_file)

def save_content(file_path, output_file):
    with open(file_path, 'r', encoding='utf-8') as file:
        output_file.write(f"{file_path} содержимое:\n")
        output_file.write(file.read())

root_directory = r'C:\Users\user\Documents\GitHub\niki_speck\my-visual-novel\src'
remove_pycache(root_directory)
output_file_path = os.path.join(root_directory, 'project_structure.txt')
save_structure(root_directory, output_file_path)
print(f"Структура проекта сохранена в файл: {output_file_path}")
print("Добро")