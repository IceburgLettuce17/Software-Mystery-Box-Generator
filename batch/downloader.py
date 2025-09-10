import requests
import random
import os
import string

def download_ninite(program_txt_path, base_url="http://ninite.com/", output_filename=os.getcwd() + "/../output/your_ninite.exe"):
    try:
        with open(program_txt_path, 'r') as f:
            all_strings = [line.strip() for line in f if line.strip()] # Read and clean strings
    except FileNotFoundError:
        print(f"Error: Text file not found at {program_txt_path}")
        return

    if len(all_strings) < 5:
        print("Error: Not enough unique strings in the text file to choose 5 random ones.")
        return

    # Choose 5 unique random strings
    random_strings = random.sample(all_strings, 5)

    # Construct the full URL
    # Assuming the random strings are separated by '/' in the URL
    full_url = os.path.join(base_url, *random_strings)
    full_url = full_url.replace("\\", "-");
    full_url = full_url + "/ninite.exe"
    print(f"Attempting to download from URL: {full_url}")

    try:
        response = requests.get(full_url, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        with open(output_filename, 'wb') as out_file:
            for chunk in response.iter_content(chunk_size=8192):
                out_file.write(chunk)
        print(f"File downloaded successfully as {output_filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error during download: {e}")

# Example usage:
if __name__ == "__main__":

    text_file = "/../possible_ninites.txt"
    # Replace with your actual base URL
    base_url = "http://ninite.com/"
    output_file = os.getcwd() + "/../output/your_ninite.exe"

    download_ninite(text_file, base_url, output_file)