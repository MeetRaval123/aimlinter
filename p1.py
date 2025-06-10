from bs4 import BeautifulSoup
def load_html(file_path):
    with open(file_path, "r" ,encoding='utf-8') as f:
        content = f.read()
        return content
html_content = load_html('meet.html')
soup = BeautifulSoup(html_content)
print(soup)
