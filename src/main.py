import os
import shutil
from pathlib import Path

import extract_title
from markdown_to_html import (
    markdown_to_html_node

)

source = "./static/"
destination = "./public/"

content = "./content/"
template = "./template.html"

def main():
    copy_from_static_to_public(source, destination)
    generate_pages_recursive(
        content, 
        template, 
        destination,
    )




def copy_from_static_to_public(source, destination):
    try:
        if os.path.exists(destination):
            shutil.rmtree(destination)

        if not os.path.exists(destination):
            os.mkdir(destination)

        dest = shutil.copytree(source, destination, dirs_exist_ok=True)

        print("After copying file:")
        print(os.listdir(dest))

        print("Destination path:", destination)
        print("Source path:", source)


    # If there is any permission issue
    except PermissionError:
        print("Permission denied.")


def generate_page(from_path, template_path, dest_path):
    print("Generating page from", from_path, "to", dest_path, "using template", template_path)

    from_file = open(from_path, "r")
    file_contents = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template_contents = template_file.read()
    template_file.close()

    
    node = markdown_to_html_node(file_contents)
    html = node.to_html()

    title = extract_title.extract_title(file_contents)
    template_contents = template_contents.replace("{{ Title }}", title).replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template_contents)


def generate_pages_recursive(content, template, dest_path):
    for item in os.listdir(content):
        # Determine full paths
        item_path = os.path.join(content, item)
        dest_item_path = os.path.join(dest_path, item)
        if os.path.isdir(item_path):
            generate_pages_recursive(item_path, template, dest_item_path)
        elif item.endswith(".md"):
            # Change file extension from .md to .html
            dest_item_path = Path(dest_item_path).with_suffix(".html")
            generate_page(item_path, template, dest_item_path)


if __name__ == "__main__":
    main()