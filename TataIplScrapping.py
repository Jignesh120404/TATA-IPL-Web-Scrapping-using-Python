import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://www.iplt20.com/auction#:~:text=204%20players%20were%20sold%20and,IPL)%202022%20Auction%20in%20Bengaluru"
r= requests.get(url)
#print(r)
soup = BeautifulSoup(r.text,"lxml")
#print(soup)
table = soup.find("table",class_="ih-td-tab auction-tbl")
title = table.find_all("th")
rows = table.find_all("tr")
header=[]

for i in title:
    name = i.text 
    header.append(name)
    
df = pd.DataFrame(columns = header)  

for i in rows[1:]:
 first_td = i.find_all("td")[0].find("div",class_="ih-pt-ic").text.strip()
 data = i.find_all("td")[1:]  
 row = [tr.text for tr in data]
 row.insert(0,first_td)
 l= len(df)
 df.loc[l]=row
excel_file_path = 'output.xlsx'
df.to_excel(excel_file_path, index=False)
    



    