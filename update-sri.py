import hashlib
import base64
import re

# Paths to your main.js and index.html files
main_js_path = "src/proj/main.js"  # Update this to match your index.html script src
index_html_path = "src/proj/index.html"  # Adjust this if needed

def generate_sri_hash(file_path):
    """Generates a SHA256 SRI hash for the given file."""
    with open(file_path, "rb") as f:
        file_data = f.read()
    sha256_hash = hashlib.sha256(file_data).digest()
    return "sha256-" + base64.b64encode(sha256_hash).decode('utf-8')

def update_html(integrity_hash):
    """Updates index.html with the new SRI hash."""
    with open(index_html_path, "r") as f:
        html_content = f.read()

    # Use regex to find and update the integrity attribute in the script tag
    # We will replace the entire integrity attribute to avoid appending
    script_tag_pattern = re.compile(r'(<script src="main.js" integrity=")([^"]+)(")', re.IGNORECASE)

    if script_tag_pattern.search(html_content):
        # Replace the integrity attribute with the new one
        new_html_content = script_tag_pattern.sub(f'\\1{integrity_hash}\\3', html_content)

        # Write the updated HTML content back to index.html
        with open(index_html_path, "w") as f:
            f.write(new_html_content)

        print(f"Updated {index_html_path} with new integrity hash: {integrity_hash}")
    else:
        print(f"Script tag for main.js not found or integrity attribute missing in {index_html_path}")


def main():
    # Generate new SRI hash for main.js
    integrity_hash = generate_sri_hash(main_js_path)

    # Update index.html with the new integrity hash
    update_html(integrity_hash)

if __name__ == "__main__":
    main()
