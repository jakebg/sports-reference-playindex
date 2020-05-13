import time

from url_finder import *
from soupify import *
# URL = 'https://www.pro-football-reference.com/play-index/psl_finder.cgi?request=1&match=single&draft=1&year_min=2019&year_max=2019&season_start=1&season_end=-1&pos%5B%5D=qb&draft_year_min=1936&draft_year_max=2020&draft_slot_min=1&draft_slot_max=500&draft_pick_in_round=pick_overall&conference=any&draft_pos%5B%5D=qb&c1stat=pass_cmp&c1comp=gt&c2stat=pass_att&c2comp=gt&c3stat=pass_inc&c3comp=gt&c4stat=pass_cmp_perc&c4comp=gt&c5stat=pass_yds&c5comp=gt&c5val=1.0&order_by=pass_td'
# page = requests.get(URL)

# text_file = open("page.html", "wb")
# text_file.write(page.content)
# text_file.close()

test_csv_dict = {'match_choice' : 'single', 
        'first_year' : '2010', 
        'last_year' : '2019', 
        'season_start_int' : '1', 
        'season_end_int' : '-1',
        'position_id' : 'qb', 
        'draft_year_begin' : '1936', 
        'draft_year_end' : '2020',
        'draft_slot_begin' : '1', 
        'draft_slot_end' : '500', 
        'draft_pick_round' : 'pick_overall',
        'draft_college_conf' : 'any',
        'draft_college_pos' : 'qb',
        'order_by_stat' : 'pass_td',
        'offset' : '1000',
        }

# URL = create_url(test_csv_dict)
# soupify(URL)
url_list = offset_loop(test_csv_dict)
for x in url_list:
    time.sleep(3)
    soupify(x)


#print(create_url(test_csv_dict))

# page = requests.get('https://www.pro-football-reference.com/play-index/psl_finder.cgi?request=1&match=single&draft=1&year_min=2015&year_max=2019&season_start=1&season_end=-1&pos[]=qb&pos[]=rb&pos[]=wr&pos[]=te&pos[]=e&pos[]=t&pos[]=g&pos[]=c&pos[]=ol&draft_year_min=1936&draft_year_max=2020&type=B&draft_slot_min=1&draft_slot_max=500&draft_pick_in_round=pick_overall&conference=any&draft_pos[]=qb&draft_pos[]=rb&c1stat=pass_cmp&c1comp=gt&c2stat=pass_att&c2comp=gt&c3stat=pass_inc&c3comp=gt&c4stat=pass_cmp_perc&c4comp=gt&c5stat=pass_yds&c5comp=gt&c5val=1.0&order_by=pass_td&offset=400')

# soup = BeautifulSoup(page.content, 'html.parser')
# for elem in soup(text = 'Sorry, there are no results that match your search.'):
#     print('I found end')