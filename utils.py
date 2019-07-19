import glob
import os
from jinja2 import Template


def new():
    content = "content/new_content_page.html"
    output = "New Content!"
    open(content, "w+").write(output)


def build():
    # loop through the files in content directory
    all_html_files = glob.glob("content/*.html")
    print(all_html_files)
    
    # build up content from empty list
    pages = []
    for html_file in all_html_files:
        # modify and extract useful parts from file paths
        # file_path = "content/bio.html"
        file_name = os.path.basename(html_file)
        print(file_name)
        name_only, extension = os.path.splitext(file_name)
        print(name_only)
        input = "content/" + file_name
        output = "docs/" + file_name
        pages.append({
                     "filename": input,
                     "output": output,
                     "title": name_only.capitalize(),
                     },)
        print(pages)
    
    # loop through files in pages list
    for page in pages:
        # jinja2 templating
        file = open(page["filename"]).read()
        template_html = open("templates/base.html").read()
        template = Template(template_html)
        output = template.render(title=page["title"], content=file, pages=pages)
        open(page["output"], "w+").write(output)

