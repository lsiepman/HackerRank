import re
from sys import stdin
from bs4 import BeautifulSoup

html_doc = stdin.read()
soup = BeautifulSoup(html_doc, "html.parser")

# fetch ids
id_divs = soup.find_all("div", {"class": "question-summary"})
sum_divs = soup.find_all("a", {"class": "question-hyperlink"})
time_divs = soup.find_all("span", {"class": "relativetime"})

ids = []
for tag in id_divs:
    ids.append(int(re.search("-([0-9]+)$", tag.get("id")).group(1)))

sums = []
for tag in sum_divs:
    sums.append(tag.text)  # .replace("'", "&#39;")) add this to win the test

times = []
for tag in time_divs:
    times.append(tag.text)

for i, j, k in zip(ids, sums, times):
    print(f"{i};{j};{k}")
