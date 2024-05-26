import os
import shutil


def main():
    # Replace the placeholder with the Python script content
    with open("src/main.py", "r") as script_file:
        python_script = script_file.read()

    with open("src/index_template.html", "r") as template_file:
        html_template = template_file.read()

    html_content = html_template.replace(
        "<!-- PYTHON_SCRIPT_PLACEHOLDER -->", python_script
    )

    # Write output to dist
    os.makedirs("dist", exist_ok=True)
    with open("dist/index.html", "w") as output_file:
        output_file.write(html_content)

    shutil.copy("src/index.css", "dist/index.css")

    # Print success message
    print("dist/index.html and dist/index.css have been created.")


if __name__ == "__main__":
    main()
