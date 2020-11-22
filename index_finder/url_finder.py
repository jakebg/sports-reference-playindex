'''
'https://www.pro-football-reference.com/play-index/psl_finder.cgi?request=1&
match=single&                           MATCH               = single, combined, total
draft=1&                                DRAFT               = ALWAYS 1
year_min=2019&                          YEAR_MIN            = first year
year_max=2019&                          YEAR_MAX            = end year
season_start=1&                         SEASON_START        = from players x season
season_end=-1&                          SEASON_END          = to players x season
pos%5B%5D=qb&                           POSITION            = CAN HAVE MULTIPLE &pos[]=qb& pos[]=rb&
                                                                QB, RB, WR, YE, E, T, G, C, OL, DT, DE,
                                                                DL, ILD, OLB, LB, CB, S, DB, K, P
draft_year_min=1936&                    DRAFT_YEAR_MIN      = player drafted from year x
draft_year_max=2020&                    DRAFT_YEAR_MAX      = player drafted to year x
draft_slot_min=1&                       DRAFT_SLOT_MIN      = player drafted from pick x in draft
draft_slot_max=500&                     DRAFT_SLOT_MAX      = player drafted to pick x in draft
                                                          1-500 all
draft_pick_in_round=pick_overall&       #######
conference=any&                         DRAFT_CONFERENCE    = college conference
draft_pos%5B%5D=qb&                     DRAFT_POSITION      = football position drafted at

                                #### Begin of extra stats
c1stat=pass_cmp& 
c1comp=gt&
c2stat=pass_att&
c2comp=gt&
c3stat=pass_inc&
c3comp=gt&
c4stat=pass_cmp_perc&
c4comp=gt&
c5stat=pass_yds&
c5comp=gt&
c5val=1.0&
                                #### End of extra stats
order_by=pass_td&                       ORDER_BY            = order the table by ceratin stat     
offset=100                              OFFSET              = table offset, 0 = first table page
                                                                sports reference, per html page, only show 100 rows
'''

# URL = 'https://www.pro-football-reference.com/play-index/psl_finder.cgi?request=1&match=single&draft=1&year_min=2019&year_max=2019&season_start=1&season_end=-1&pos%5B%5D=qb&draft_year_min=1936&draft_year_max=2020&draft_slot_min=1&draft_slot_max=500&draft_pick_in_round=pick_overall&conference=any&draft_pos%5B%5D=qb&c1stat=pass_cmp&c1comp=gt&c2stat=pass_att&c2comp=gt&c3stat=pass_inc&c3comp=gt&c4stat=pass_cmp_perc&c4comp=gt&c5stat=pass_yds&c5comp=gt&c5val=1.0&order_by=pass_td'
# page = requests.get(URL)

# text_file = open("page.html", "wb")
# text_file.write(page.content)
# text_file.close()


# INPUTS
match_choice        = 'single'
    # from year
first_year          = '2010'
    # to year
last_year           = '2019'

    # which season in career to start from, xth career season
season_start_int    = '1'
    # which season in career to end from, xth carrer season        
season_end_int      = '-1'

    # position the player plays
position_id         = 'qb' # could chain multiple positions

            ## DRAFT 
    # which drafts to select from
draft_year_begin    = '1936'
draft_year_end      = '2020'
    # which spot in draft player was picked
draft_slot_begin    = '1'
draft_slot_end      = '500'
    # which round picked in, 
draft_pick_round    = 'pick_overall'
    # which college conference played in
draft_college_conf  = 'any'
    # which position was player drafted as
draft_college_pos   = 'qb' # could chain multiple position

# order table by
order_by_stat       = 'pass_td'
offset             = '000'

dict = { 'match_choice'     : match_choice, 
        'first_year'        : first_year, 
        'last_year'         : last_year, 
        'season_start_int'  : season_start_int, 
        'season_end_int'    : season_end_int,
        'position_id'       : position_id, 
        'draft_year_begin'  : draft_year_begin, 
        'draft_year_end'    : draft_year_end,
        'draft_slot_begin'  : draft_slot_begin, 
        'draft_slot_end'    : draft_slot_end, 
        'draft_pick_round'  : draft_pick_round,
        'draft_college_conf': draft_college_conf,
        'draft_college_pos' : draft_college_pos,
        'order_by_stat'     : order_by_stat,
        'offset'            : offset,
        }

''' 
Creates a url given a dictionary

    Parameters 
        input_dict : 
            match_choice : 

            first_year : int
                from season

            last_year  : int
                 to season

            season_start_int
                which season in career to start from 

            season_end_int 
                which season in career to end from

            position_id  # could chain multiple positions
                position the player plays

            draft_year_begin 
                which drafts to start from

            draft_year_end 
                which drafts to end to

            draft_slot_begin
            draft_slot_end
                which spot in draft player was picked

            draft_pick_round 
                which round player picked in

            draft_college_conf 
                which college conference player played in

            draft_college_pos # could chain multiple position
                which position was player drafted as

            order_by_stat
                order table by a certain stat

    Returns
        a url that redirects to sports reference page

'''
def create_url(input_dict):
    main_url            = 'https://www.pro-football-reference.com/'
    play_index          = 'play-index/psl_finder.cgi?request=1&'
    MATCH               = 'match=' + input_dict['match_choice'] + '&'
    DRAFT               = 'draft=1&'
    YEAR_MIN            = 'year_min=' + input_dict['first_year'] + '&'
    YEAR_MAX            = 'year_max=' + input_dict['last_year'] + '&'
    SEASON_START        = 'season_start=' + input_dict['season_start_int'] + '&'
    SEASON_END          = 'season_end='+ input_dict['season_end_int'] + '&'
    POSITION            = 'pos[]=' + input_dict['position_id'] + '&'
    DRAFT_YEAR_MIN      = 'draft_year_min=' + input_dict['draft_year_begin'] + '&'
    DRAFT_YEAR_MAX      = 'draft_year_max=' + input_dict['draft_year_end'] + '&'
    DRAFT_SLOT_MIN      = 'draft_slot_min=' + input_dict['draft_slot_begin'] + '&'
    DRAFT_SLOT_MAX      = 'draft_slot_max=' + input_dict['draft_slot_end'] + '&'
    DRAFT_PICK_IN_ROUND = 'draft_pick_in_round=' + input_dict['draft_pick_round'] + '&'
    DRAFT_CONFERENCE    = 'conference=' + input_dict['draft_college_conf'] + '&'
    DRAFT_POSITION      = 'draft_pos[]=' + input_dict['draft_college_pos'] + '&'
    ### EXTRA STATS HERE

    ### END EXTRA STATS
    ORDER_BY            = 'order_by=' + input_dict['order_by_stat'] + '&'
    


        
    
    full_url = main_url + play_index + MATCH + DRAFT + YEAR_MAX + YEAR_MIN + SEASON_START + SEASON_END +\
    POSITION + DRAFT_YEAR_MIN + DRAFT_YEAR_MAX + DRAFT_SLOT_MIN + DRAFT_SLOT_MAX + DRAFT_PICK_IN_ROUND +\
    DRAFT_CONFERENCE + DRAFT_POSITION + ORDER_BY


    ### TESTING OFFSET
    OFFSET_NUMBER   = input_dict['offset']

    OFFSET              = 'offset=' + OFFSET_NUMBER

    full_url += OFFSET

    print(full_url)
    return full_url

# Sports reference offset is set by 100 table rows in one page. 
# Have to loop through offsets to get all table entries
def offset_loop(input_dict):
    OFFSET_NUMBER   = input_dict['offset']
    offset_int = int(int(OFFSET_NUMBER)/100)

    url_list = []

    for x in range(offset_int):
        input_dict['offset'] = str(x*100)
        url_list.append(create_url(input_dict))
    return url_list







# TEST DICT
test_dict = {'match_choice' : 'single', 
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
        }

# test_url = create_url(test_dict)

# if test_url != 'https://www.pro-football-reference.com/play-index/psl_finder.cgi?request=1&match=single&draft=1&year_max=2019&year_min=2010&season_start=1&season_end=-1&pos[]=qb&draft_year_min=1936&draft_year_max=2020&draft_slot_min=1&draft_slot_max=500&draft_pick_in_round=pick_overall&conference=any&draft_pos[]=qb&order_by=pass_td&':
#     raise Exception('NO GOOD')

#another = create_url(dict)
#print(another)
