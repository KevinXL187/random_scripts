import pandas as pd
import json, os

def json_to_csv(in_file, out_file):
    try:
        with open(in_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        df = pd.DataFrame(data)
        df.to_csv(out_file, index=False)
        print("Successfully converted")
    
    except FileNotFoundError:
        print(f"Error: File '{in_file}' not found. Check the path.")
    except json.JSONDecodeError:
        print(f"Error: '{in_file}' is not a valid JSON file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def combineJson(dir, out_file):
    files = [f for f in os.listdir(dir) if f.endswith('.json')]
    combined_data = []
    
    for file in files:
        file_path = os.path.join(dir, file)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

                # Handle nested Spotify data (e.g., endsong_X.json)
                if isinstance(data, dict) and "items" in data:
                    data = data["items"]

                combined_data.extend(data)
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
           
    pd.DataFrame(combined_data).to_json(out_file, index=False)
    print(f"Combined {len(files)} files successfully")
    
if __name__ == "__main__":
    print("Converter")
    print("---------")

    converter = input("Enter Function To Use: ").strip()
    if converter.lower() in ["jsontocsv", "j2csv"]:
        para1 = input("Input JSON file path: ").strip()
        para2 = input("Output CSV file name: ").strip()

        if not para2.lower().endswith('.csv'):
            para2 += '.csv'
        json_to_csv(para1, para2)

    elif converter.lower() in ["combinejson", "cjson"]:
        para1 = input("Input folder path").strip()
        para2 = input("Output Json file name: ").strip()

        if not para2.lower().endswith('.json'):
            para2 += '.json'
        combineJson(para1, para2)