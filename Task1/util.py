import os
import yaml
import shutil

def read_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)
    return content if content is not None else {}
    
def write_yaml(file_path, content):
    with open(file_path, 'w') as file:
        yaml.safe_dump(content, file, default_flow_style=False, sort_keys=False)

def modifications(content, updates):
    if isinstance(content, dict):
        for key, value in updates.items():
            if key in content:
                if isinstance(value, dict) and isinstance(content[key], dict):
                    modifications(content[key], value)
                else:
                    content[key] = value
    elif isinstance(content, list):
        for item in content:
            if isinstance(item, dict):
                modifications(item, updates)
    return content

def apply_list_modifications(content_list, updates_list):
    updated_list = content_list[:]
    
    for update in updates_list:
        if isinstance(update, dict):
            index = update.get('index')
            item_updates = update.get('update', {})

            if index is not None and 0 <= index < len(updated_list):
                updated_list[index] = modifications(updated_list[index], item_updates)
        # If update is not a dict or does not contain 'index', ignore it
        # No changes are made if update does not match expected structure
    
    return updated_list


def process_files(src_folder, dest_folder, updates):
    for root, _, files in os.walk(src_folder):
        for file_name in files:
            if file_name.endswith('.yaml'):
                src_file_path = os.path.join(root, file_name)
                ## relative_path = os.path.relpath(src_file_path, src_folder)
                dest_file_path = os.path.join(dest_folder, src_file_path)
                os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)
                content = read_yaml(src_file_path)
                updated_content = modifications(content, updates)
                write_yaml(dest_file_path, updated_content)
                
def main(src_folder, dest_folder, updates):
    if os.path.exists(dest_folder):
        shutil.rmtree(dest_folder)
    os.makedirs(dest_folder)
 
    process_files(src_folder, dest_folder, updates)

