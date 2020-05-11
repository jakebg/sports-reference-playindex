import requests
from bs4 import BeautifulSoup

# URL = 'https://www.pro-football-reference.com/play-index/psl_finder.cgi?request=1&match=single&draft=1&year_min=2019&year_max=2019&season_start=1&season_end=-1&pos%5B%5D=qb&draft_year_min=1936&draft_year_max=2020&draft_slot_min=1&draft_slot_max=500&draft_pick_in_round=pick_overall&conference=any&draft_pos%5B%5D=qb&c1stat=pass_cmp&c1comp=gt&c2stat=pass_att&c2comp=gt&c3stat=pass_inc&c3comp=gt&c4stat=pass_cmp_perc&c4comp=gt&c5stat=pass_yds&c5comp=gt&c5val=1.0&order_by=pass_td'
# page = requests.get(URL)

# text_file = open("page.html", "wb")
# text_file.write(page.content)
# text_file.close()

text_file = open("page.html", "r")

soup = BeautifulSoup(text_file, 'html.parser')
#print(soup.contents)
#results = soup.find(data_stat="")
#print(results.prettify())
def check_none(x):
    if x is None:
        return False
    else:
        return True


new_html = open("new_html.html", "w")

csv_file = open("csvfile.csv","a")

# stats to get from html file
stat_array = ['ranker', 'player', 'year_id', 'age', 'team']

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
