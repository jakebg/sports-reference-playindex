from bs4 import BeautifulSoup
import requests

stat_array = ['ranker', 'player', 'year_id', 'age', 'team', 'pass_td']
csv_file = open("csvfile.csv","a")

def check_none(x):
    if x is None:
        return False
    else:
        return True

text_file = open("new_html.html", "r")

def write_csv(_soup_page):
    div_ = _soup_page.find_all('div', class_="table_outer_container")

    for job_elem in div_:
        # skip the table headers in the middle of the table
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

def check_last(_soup_page):
    for elem in _soup_page(text = 'Sorry, there are no results that match your search.'):
        print('Found sorry, ending')
        return False
    return True

def soupify(URL_FOR_SOUP):
    page = requests.get(URL_FOR_SOUP)
    html = page.text
    soup = BeautifulSoup(html, 'html.parser')
    #print(soup.contents)
    #results = soup.find(data_stat="")
    #print(results.prettify())
    # stats to get from html file
    if check_last(soup):
        write_csv(soup)


        