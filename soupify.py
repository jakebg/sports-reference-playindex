from bs4 import BeautifulSoup
import requests

def check_none(x):
    if x is None:
        return False
    else:
        return True

def soupify(URL_FOR_SOUP):
    page = requests.get(URL_FOR_SOUP)

    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup.contents)
    #results = soup.find(data_stat="")
    #print(results.prettify())

    csv_file = open("csvfile.csv","a")

    # stats to get from html file
    stat_array = ['ranker', 'player', 'year_id', 'age', 'team', 'pass_td']

    div_ = soup.find_all('div', class_="table_outer_container")
    for job_elem in div_:
    # hacky way to bypass the table headers in the middle of the table
        wrappers=job_elem.find_all('tr', attrs={'class': ''})

        for x in wrappers:
            for y in stat_array:
                test = x.find(attrs={'data-stat': y})
                csv_file.write(test.text)
                csv_file.write(',')
            csv_file.write('\n')
            if not check_none(test):
                print('test')
                continue