import requests
import lxml.html

cp = 0
concerts = {}

for cp in range(0, 8451, 130):
    print(cp//130)
    result = requests.get("http://darkside.ru/show/index.phtml?cp={0}".format(cp))
    page = lxml.html.fromstring(result.text)
    #Bold links
    elements = page.find_class('titleshow')

    for elem in elements:
        groups = elem.text_content().lower().split(', ')
        for group in groups:
            if group in concerts.keys():
                concerts[group] += 1
            else:
                concerts[group] = 1

    #Usual link
    elements = page.find_class('titles')
    for elem in elements:
        link = elem.findall('.//a').pop()
        groups = link.text_content().lower().split(', ')
        for group in groups:
            if group in concerts.keys():
                concerts[group] += 1
            else:
                concerts[group] = 1

sorted_groups = sorted(list(concerts.items()), key=lambda x:x[1], reverse=True)
for group in sorted_groups:
    print("{0} - {1}".format(group[0], group[1]))
