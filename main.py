# Imports
from selenium import webdriver
import pandas as pd
import csv



# Driver SetUp and driver "GET" method

chrome_driver_path = "C:/Development/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://stats.espncricinfo.com/ci/engine/records/index.html")

# Stats_Guru Path
stats_guru = driver.find_element_by_xpath('//*[@id="subnav_tier1"]/li[1]/a')
stats_guru.click()

# Search for a particular team and click search

search_name = "INDIA"
search_box = driver.find_element_by_xpath('//*[@id="ciHomeContentlhs"]/div[3]/div[13]/form/input[1]')
search_box.send_keys(search_name)
search_button = driver.find_element_by_xpath('//*[@id="ciHomeContentlhs"]/div[3]/div[13]/form/input[2]')
search_button.click()
search = driver.find_element_by_id("team")
search.click()

# Different paths for interaction

combined_stats_path = '//*[@id="gurusearch_team"]/table/tbody/tr[1]/td[3]/a[4]'
home_venue_path = '//*[@id="ciHomeContentlhs"]/div[3]/table[1]/tbody/tr/td/table/tbody/tr[2]/' \
                  'td/form/table/tbody/tr[4]/td[2]/label[1]/input'
away_venue_path = '//*[@id="ciHomeContentlhs"]/div[3]/table[1]/tbody/tr/td/table/tbody/tr[2]/' \
                  'td/form/table/tbody/tr[4]/td[2]/label[2]/input'
neutral_venue_path = '//*[@id="ciHomeContentlhs"]/div[3]/table[1]/tbody/tr/td/table/tbody/tr[2]/' \
                     'td/form/table/tbody/tr[4]/td[2]/label[3]/input'
quick_pick_path = '//*[@id="ciHomeContentlhs"]/div[3]/table[1]/tbody/tr/td/table/tbody/tr[2]/' \
                  'td/form/table/tbody/tr[7]/td[2]/select'
quick_pick_10years_path = '//*[@id="ciHomeContentlhs"]/div[3]/table[1]/tbody/tr/td/table/tbody/tr[2]/' \
                          'td/form/table/tbody/tr[7]/td[2]/select/option[9]'
won_match_check_path = '//*[@id="ciHomeContentlhs"]/div[3]/table[1]/tbody/tr/td/table/tbody/tr[2]/' \
                       'td/form/table/tbody/tr[9]/td[2]/label[1]/input'
lost_match_check_path = '//*[@id="ciHomeContentlhs"]/div[3]/table[1]/tbody/tr/td/table/tbody/tr[2]/' \
                        'td/form/table/tbody/tr[9]/td[2]/label[2]/input'
drawn_match_check_path = '//*[@id="ciHomeContentlhs"]/div[3]/table[1]/tbody/tr/td/table/tbody/tr[2]/' \
                         'td/form/table/tbody/tr[9]/td[2]/label[4]/input'
tied_match_check_path = '//*[@id="ciHomeContentlhs"]/div[3]/table[1]/tbody/tr/td/table/tbody/tr[2]/' \
                        'td/form/table/tbody/tr[9]/td[2]/label[3]/input'
no_result_match_check_path = '//*[@id="ciHomeContentlhs"]/div[3]/table[1]/tbody/tr/td/table/tbody/tr[2]/' \
                             'td/form/table/tbody/tr[9]/td[2]/label[5]/input'
query_result_filter_path = '//*[@id="ciHomeContentlhs"]/div[3]/table[1]/tbody/tr/td/table/tbody/tr[2]/' \
                           'td/form/table/tbody/tr[10]/td[2]/' \
                           'table/tbody/tr[2]/td[1]/label[3]/input'
team_total_filter = '//*[@id="ciHomeContentlhs"]/div[3]/table[1]/tbody/tr/td/table/tbody/tr[2]/' \
                    'td/form/table/tbody/tr[11]/td[2]/label[1]/input'
submit_query_path = '//*[@id="ciHomeContentlhs"]/div[3]/table[1]/tbody/tr/td/table/tbody/tr[2]/' \
                    'td/form/table/tbody/tr[12]/td[2]/table/tbody/tr/td[1]/input'

# Finding the elements with above paths and interacting with them

combined_stats = driver.find_element_by_xpath(combined_stats_path)
combined_stats.click()
home_venue = driver.find_element_by_xpath(home_venue_path)
home_venue.click()
away_venue = driver.find_element_by_xpath(away_venue_path)
away_venue.click()
neutral_venue = driver.find_element_by_xpath(neutral_venue_path)
neutral_venue.click()
quick_pick = driver.find_element_by_xpath(quick_pick_path)
quick_pick.click()
quick_pick_10years = driver.find_element_by_xpath(quick_pick_10years_path)
quick_pick_10years.click()
won_match = driver.find_element_by_xpath(won_match_check_path)
won_match.click()
lost_match = driver.find_element_by_xpath(lost_match_check_path)
lost_match.click()
drawn_match = driver.find_element_by_xpath(drawn_match_check_path)
drawn_match.click()
tied_match = driver.find_element_by_xpath(tied_match_check_path)
tied_match.click()
no_result_match = driver.find_element_by_xpath(no_result_match_check_path)
no_result_match.click()
query_match_result = driver.find_element_by_xpath(query_result_filter_path)
query_match_result.click()
submit_query = driver.find_element_by_xpath(submit_query_path)
submit_query.click()

# Getting the required data from the search results created and manipulating the data

all_data = driver.find_elements_by_css_selector('tr.data1')
all_data_list = []
for data in all_data:
    value = data.text
    all_data_list.append(value)

all_data_list.pop(0)
all_data_list.pop(0)
for n in range(len(all_data_list)):
    all_data_list[n] = all_data_list[n].replace("Test #", "$")
    all_data_list[n] = all_data_list[n].replace("T20I #", "$")
    all_data_list[n] = all_data_list[n].replace("ODI #", "$")
    if "$" in all_data_list[n]:
        all_data_list[n] = all_data_list[n][0:all_data_list[n].index("$")]
    all_data_list[n] = all_data_list[n].replace(" ", ",")
    all_data_list[n] = all_data_list[n].split(",")
    all_data_list[n].pop(-1)

# More manipulation.....

check_list = ["TestvWest", "ODIvWest", "T20IvWest", "TestvSri", "ODIvSri", "T20IvSri",
              "TestvSouth", "ODIvSouth", "T20IvSouth", "TestvNew", "ODIvNew", "T20IvNew",
              "TestvHong", "ODIvHong", "T20IvHong"]

# Even More Manipulation with Soooooo many For Loops

for n in range(len(all_data_list)):
    for word in all_data_list[n]:
        if word == "Test" or word == "ODI" or word == "T20I":
            new_word = all_data_list[n][all_data_list[n].index(word)]+all_data_list[n][all_data_list[n].index(word)+1]+all_data_list[n][all_data_list[n].index(word)+2]
            del all_data_list[n][all_data_list[n].index(word)+1:all_data_list[n].index(word)+3]
            all_data_list[n][all_data_list[n].index(word)] = new_word

for n in range(len(all_data_list)):
    for word in all_data_list[n]:
        for each in check_list:
            if word == each:
                replace_word = word + all_data_list[n][all_data_list[n].index(word) + 1]
                all_data_list[n].pop(all_data_list[n].index(word) + 1)
                all_data_list[n][all_data_list[n].index(word)] = replace_word


for n in range(len(all_data_list)):
    for word in all_data_list[n]:
        if word == "inns":
            replace = word + all_data_list[n][all_data_list[n].index(word)+1] +\
                      all_data_list[n][all_data_list[n].index(word)+2] + all_data_list[n][all_data_list[n].index(word)+3]
            del all_data_list[n][all_data_list[n].index(word)+1:all_data_list[n].index(word)+4]
            all_data_list[n][all_data_list[n].index(word)] = replace

for n in range(len(all_data_list)):
    for word in all_data_list[n]:
        if word == "runs" or word == "run" or word == "wicket" or word == "wickets" or word == "Oval":
            add_runs = all_data_list[n][all_data_list[n].index(word) - 1] + word
            all_data_list[n].pop(all_data_list[n].index(word) - 1)
            all_data_list[n][all_data_list[n].index(word)] = add_runs
for n in range(len(all_data_list)):
    for word in all_data_list[n]:
        if word == "Hyderabad" or word == "Colombo" or word == "Dublin" or word == "Dubai" or word == "Mount":
            next_word = word + all_data_list[n][all_data_list[n].index(word)+1]
            all_data_list[n].pop(all_data_list[n].index(word)+1)
            all_data_list[n][all_data_list[n].index(word)] = next_word

for n in range(len(all_data_list)):
    for word in all_data_list[n]:
        if word == "Port":
            next_word = word + all_data_list[n][all_data_list[n].index(word)+1] +\
                      all_data_list[n][all_data_list[n].index(word)+2]
            del all_data_list[n][all_data_list[n].index(word)+1:all_data_list[n].index(word)+3]
            all_data_list[n][all_data_list[n].index(word)] = next_word

for n in range(len(all_data_list)):
    if len(all_data_list[n]) % 2 != 0:
        all_data_list[n].insert(2, "-")
for n in range(len(all_data_list)):
    all_data_list[n][-3] = all_data_list[n][-3]+all_data_list[n][-2]+all_data_list[n][-1]
    del all_data_list[n][-2:]
# Writing the manipulated data to a csv file named "cric_stats.csv"

cric_stats_file = open('cric_stats.csv', 'w', newline='', encoding='utf-8')
writer = csv.writer(cric_stats_file)
writer.writerow(['Result', 'Margin', 'BR', 'Toss', 'Bat', 'Opposition',  'Ground', 'Start Date'])
for item in all_data_list:
    writer.writerow(item)
cric_stats_file.close()

# Changing 'Start Date' column data to 'DateTime' objects using Pandas.

df = pd.read_csv("cric_stats.csv")
df['Start Date'] = pd.to_datetime(df['Start Date'])
