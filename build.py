def main():
    with open("src/main.py", "r") as script_file:
        python_script = script_file.read()

    with open("index_template.html", "r") as template_file:
        html_template = template_file.read()

    html_content = html_template.replace(
        "<!-- PYTHON_SCRIPT_PLACEHOLDER -->", python_script
    )

    with open("index.html", "w") as output_file:
        output_file.write(html_content)

    print("index.html has been created with the embedded Python script.")


if __name__ == "__main__":
    main()
