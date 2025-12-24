import os

def read_and_process_file(input_filename):

    try:
        with open(input_filename, 'r') as file:
            lines = file.readlines()
            
        # Process the content (add line numbers and modify each line)
        processed_lines = []
        for i, line in enumerate(lines, 1):
            # Add line number and modify the content
            modified_line = f"Line {i}: {line.strip().upper()}\n"
            processed_lines.append(modified_line)
            
        return processed_lines
        
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{input_filename}' not found.")
    except PermissionError:
        raise PermissionError(f"Error: No permission to read file '{input_filename}'.")
    except UnicodeDecodeError:
        raise UnicodeDecodeError(f"Error: Cannot decode file '{input_filename}'. It may be a binary file.")
    except Exception as e:
        raise Exception(f"Error reading file '{input_filename}': {str(e)}")

def write_processed_file(output_filename, processed_content):

    try:
        with open(output_filename, 'w') as file:
            file.writelines(processed_content)
        return True
    except PermissionError:
        raise PermissionError(f"Error: No permission to write to file '{output_filename}'.")
    except Exception as e:
        raise Exception(f"Error writing to file '{output_filename}': {str(e)}")

def main():
    while True:
        try:
            # Get input filename from user
            input_filename = input("Enter the input filename (or 'quit' to exit): ")
            
            if input_filename.lower() == 'quit':
                print("Program terminated.")
                break
                
            # Check if file exists before processing
            if not os.path.exists(input_filename):
                print(f"Error: File '{input_filename}' does not exist.")
                continue
                
            # Generate output filename
            base_name = os.path.splitext(input_filename)[0]
            extension = os.path.splitext(input_filename)[1]
            output_filename = f"{base_name}_processed{extension}"
            
            print(f"\nProcessing '{input_filename}'...")
            
            # Read and process the file
            processed_content = read_and_process_file(input_filename)
            
            # Write to new file
            write_processed_file(output_filename, processed_content)
            
            print(f"File has been processed.")
            print(f"Original file: {input_filename}")
            print(f"Processed file: {output_filename}")
            print(f"Total lines processed: {len(processed_content)}")
            print()
            
        except FileNotFoundError as e:
            print(f" {e}")
        except PermissionError as e:
            print(f" {e}")
        except UnicodeDecodeError as e:
            print(f" {e}")
        except Exception as e:
            print(f" {e}")
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user.")
            break

if __name__ == "__main__":
    main()
