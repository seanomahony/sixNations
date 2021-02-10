from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install())

URL = 'https://www.sixnationsrugby.com/report/scotland-secure-historic-twickenham-victory#match-stats'
driver.get(URL)
player_stats = driver.find_elements_by_class_name("player-stats")
for x in range(len(player_stats)):
    # This is faulty.
    if player_stats[x].is_displayed():
        driver.execute_script("arguments[0].click();", player_stats[x])
        time.sleep(2)

page_source = driver.page_source

players_selector = pd.read_html(page_source)
df = players_selector[4]
df.drop(df.columns[df.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)
df.head()
df.to_csv(r'C:\temp\EnglandPlayersVsScotland.csv')

df2 = players_selector[5]
df2.drop(df2.columns[df2.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)
df2.head()
df2.to_csv(r'C:\temp\ScotlandPlayersVsEngland.csv')
