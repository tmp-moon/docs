import os
import shutil
import re

page = os.getenv("NOTION_PAGE", "111a77bf59b480d9b0ebfe5b3743e768")

def copy_file(file_path, file_name, destination_folder):
  splitted_path = file_path.split("/")
  real_path = ""

  for part in splitted_path:
    part_without_id = re.sub(r'[a-f0-9]{32}', '', part)
    contain_extension = "." in part_without_id
    if contain_extension:
      real_path += part_without_id + "/"
    else:
      real_path += part_without_id[0:-1] + "/"
  real_path = real_path[0:-1]
  real_path = real_path.replace(" .md", ".md")

  dest_dir = os.path.join(destination_folder, os.path.dirname(real_path))
  os.makedirs(dest_dir, exist_ok=True)

  # Construct the destination file path
  dest_file = os.path.join(destination_folder, f"{real_path}")

  # Copy the file
  shutil.copy2(file_path, dest_file)
  return real_path

def process_export_folder():
  os.chdir(f"export/Documentation {page}/")

  destination_folder = "../.."
  for root, _, files in os.walk("./"):
    for file in files:
      file_path = os.path.join(root, file)
      new_path = copy_file(file_path, file, destination_folder)
      print(f"File: {new_path} created")

  # Loop through all files in the destination folder
  for root, _, files in os.walk(destination_folder):
    for file in files:
      file_path = os.path.join(root, file)
      # Check if it's a markdown file
      if file.endswith('.md'):
        is_different = True
        while is_different:
          with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
          # Regex pattern to match the unwanted part
          pattern = r'(.*)%20([a-f0-9]{32})([\/\.].*)'

          # Replace using regex
          result = re.sub(pattern, r'\1\3', content)

          # Write the modified content back to the file
          if content != result:
            with open(file_path, 'w', encoding='utf-8') as f:
              f.write(result)
          else:
            is_different = False

if __name__ == "__main__":
  process_export_folder()