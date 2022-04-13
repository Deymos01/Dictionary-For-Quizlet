import requests
from bs4 import BeautifulSoup


def createTxtFile(data):
    with open('dictionary.txt', 'w') as file:
        for elem in data:
            line = elem[0]['word'] + '\t' + elem[0]['definition'] + '\n\nE.g.\n'
            for example in elem[0]['examples without word']:
                line += example + '\n'
            line = line[:-1] + '@'
            file.write(line)


def get_html(url, HEADERS, params=None):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def get_content(html, word):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find('div', class_='page')

    if not items:
        return 1

    description = []
    examples = []

    if items.find('div', class_='degs had lbt lb-cm'):
        emps = items.find('div', class_='degs had lbt lb-cm').find_all('span', class_='deg')
        for i in range(len(emps)):
            examples.append(emps[i].get_text()[29:-25])
            if i > 0: break
    elif items.find('div', class_='def-body ddef_b'):
        emps = items.find('div', class_='def-body ddef_b').find_all('span', class_='eg deg')
        for i in range(len(emps)):
            examples.append(emps[i].get_text())
            if i > 0: break
    else:
        examples = "Example not found"

    # 'transcription': items.find('span', class_='pron dpron').get_text()
    description.append({
        'word': word,
        'definition': items.find('div', class_='def ddef_d db').get_text(),
        'examples': examples,
        'examples without word': [x.replace(word, '_' * len(word)) for x in examples]
    })

    if description[0]['definition'][-2:] == ": ":
        description[0]['definition'] = description[0]['definition'][:-2]

    return description


def parse(URL, HEADERS, word):
    html_page = get_html(URL, HEADERS)
    if html_page.status_code == 200:
        return get_content(html_page.text, word)
    else:
        return 1


def main(dictionary=None):
    # Check the user word for misprint
    # if dictionary == None:
    #     while True:
    #         word = input("Input a term: ")
    #         if any(x in string.digits + string.punctuation for x in list(word)):
    #             print("Your word contains digits or special symbols. Remove it.")
    #         else:
    #             word = word.lower().replace(" ", "-")
    #             break
    #     dictionary = [word]
    description = []
    counter = 0
    for elem in dictionary:
        elem = elem.lower()
        URL = "https://dictionary.cambridge.org/us/dictionary/english/" + elem
        HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0',
                   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'}

        adding = parse(URL, HEADERS, elem)
        if adding != 1:
            description.append(adding)
        else:
            counter += 1
    if description:
        createTxtFile(description)
    return counter


if __name__ == "__main__":
    pass
