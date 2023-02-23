from bs4 import BeautifulSoup
with open('./test.html') as fin:
    html_doc = fin.read()

print(html_doc)
print('#' * 30)

soup = BeautifulSoup(html_doc,"html.parser")
