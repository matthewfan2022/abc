#!/usr/bin/env python3
"""
Script to parse test.jsonl into an array of JSON objects
"""

import json
import sys

def parse_jsonl_to_array(file_path):
    """
    Parse a JSONL file into an array of JSON objects
    
    Args:
        file_path (str): Path to the JSONL file
        
    Returns:
        list: Array of JSON objects
    """
    json_objects = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                if line:  # Skip empty lines
                    try:
                        json_obj = json.loads(line)
                        json_objects.append(json_obj)
                    except json.JSONDecodeError as e:
                        print(f"Error parsing line {line_num}: {e}")
                        print(f"Line content: {line[:100]}...")  # Show first 100 chars
                        continue
                        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
    
    return json_objects

def main():
    file_path = "/Users/matthewfan/Desktop/abc/test.jsonl"
    
    print(f"Parsing {file_path}...")
    json_array = parse_jsonl_to_array(file_path)
    
    if json_array is not None:
        print(f"Successfully parsed {len(json_array)} JSON objects")
        
        # Save the parsed array to a new JSON file
        output_file = "/Users/matthewfan/Desktop/abc/parsed_objects.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(json_array, f, indent=2, ensure_ascii=False)
        
        print(f"Saved parsed objects to {output_file}")
        
        # Show some statistics
        print(f"\nStatistics:")
        print(f"- Total objects: {len(json_array)}")
        
        # Show first object structure
        if json_array:
            print(f"\nFirst object keys: {list(json_array[0].keys())}")
            
            # Count different types
            types = {}
            for obj in json_array:
                obj_type = obj.get('type', 'unknown')
                types[obj_type] = types.get(obj_type, 0) + 1
            
            print(f"\nObject types:")
            for obj_type, count in types.items():
                print(f"  {obj_type}: {count}")
    else:
        print("Failed to parse the file")

if __name__ == "__main__":
    main()
