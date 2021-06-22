from bs4 import BeautifulSoup
import requests
import os

url = 'https://cses.fi/problemset/'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
content = soup.find('div', class_='content')

problem_sets = dict()
set_name = content.contents[4]
while True:
    problem_list = set_name.next_sibling
    problem_sets[set_name.string] = list()
    for link in problem_list.find_all('a'):
        problem_sets[set_name.string].append(link.get('href'))
    set_name = problem_list.next_sibling
    if set_name.name == 'table':
        break

for j, (set_name, links) in enumerate(problem_sets.items()):
    os.makedirs(f'{j+1} {set_name}')
    for i, link in enumerate(links):
        problem_page = requests.get(f'https://cses.fi{link}')
        soup = BeautifulSoup(problem_page.content, 'html.parser')
        content = soup.find('div', class_='content')
        problem_name = content.title.string
        problem_text = content.text

        problem_text = problem_text.replace('$', '')
        problem_text = problem_text.replace('\le', '<=')
        problem_text = problem_text.replace('\cdot', '*')
        problem_text = problem_text.replace('\]', '')
        problem_text = problem_text.replace('\[', '')
        problem_text = problem_text.replace('\\rightarrow', '->')
        problem_text = problem_text.replace('\ldots', '...')
        problem_text = problem_text.replace('\dots', '...')
        problem_text = problem_text.replace('\\times', '*')

        f = open(f'{j+1} {set_name}/{i+1} {problem_name[7:]}.py', 'w')
        f.write(f'\'\'\'\n{problem_text}\n\'\'\'')
        f.close