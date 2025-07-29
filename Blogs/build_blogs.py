import os
import json

def generate_manifest():
    current_directory = os.getcwd()
    
    manifest = []
    id = 0
    
    for filename in os.listdir(current_directory):
        if filename.endswith('.json'):
            file_path = os.path.join(current_directory, filename)
            print(f"Processing file: {filename}")
            
            with open(file_path, 'r', encoding='utf-8') as json_file:
                try:
                    id = id + 1
                    data = json.load(json_file)
                    data['ID'] = id
                    entry = {
                        'TITLE': data.get('TITLE'),
                        'DATE': data.get('DATE'),
                        'INTERNAL': os.path.splitext(filename)[0],
                        'ID': id
                    }
                    manifest.append(entry)

                    with open(file_path, 'w', encoding='utf-8') as write_file:
                        json.dump(data, write_file, indent=4)

                except json.JSONDecodeError:
                    id = id - 1
                    print(f"Error decoding JSON from file: {filename}")
    
    for entry in manifest:
        try:
            entry['INTERNAL'] = int(entry['INTERNAL'])
            entry['ID'] = int(entry['ID'])
        except ValueError:
            print(f"Warning: Unable to convert INTERNAL '{entry['INTERNAL']}' to int")
    
    manifest.sort(key=lambda x: x['INTERNAL'], reverse=True)
    
    for entry in manifest:
        entry['INTERNAL'] = str(entry['INTERNAL'])
    
    with open('manifest.txt', 'w', encoding='utf-8') as manifest_file:
        json.dump(manifest, manifest_file, indent=4)
        
    print("Manifest generated successfully: manifest.txt")

if __name__ == "__main__":
    generate_manifest()
