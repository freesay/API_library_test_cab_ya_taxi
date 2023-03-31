import os
import json


def create_json_file(response, file_name, method):
    """
    Метод для сохранения данных в файл JSON.
    """
    folder = f'{method}_JSON'
    parent_folder = 'method_responses'
    path_to_file = os.path.join(parent_folder, folder, file_name)
    info = json.loads(response.text)
    with open(path_to_file, 'w', encoding='utf-8') as file:
        file.write(json.dumps(info, indent=4, ensure_ascii=False, skipkeys=True))
    return info


def load_data(folder, file_name):
    parent_folder = 'request_examples'
    path_to_file = os.path.join(parent_folder, folder, file_name)
    with open(path_to_file, 'r', encoding='utf-8') as file:
        data = ''
        for line in file:
            data += line.strip()
    return data.encode('utf-8')
