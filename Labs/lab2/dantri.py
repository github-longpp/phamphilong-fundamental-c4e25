import pyexcel
from urllib.request import urlopen
from bs4 import BeautifulSoup
# urllib
url = "https://dantri.com.vn"
# 1. Download the page

# 1.1 Open connection
conn = urlopen(url)
# 1.2 Read data
raw_data = conn.read()
# 1.3 Decode data
content = raw_data.decode("utf8")

# print(content)

# f = open("dantri.html" , "wb")
# f.write(raw_data)
# f.close()

# 2. Find ROI
soup = BeautifulSoup(content, "html.parser")
# print(soup.prettify())
ul_new = soup.find("ul" , "ul1 ulnew")


# 3. Copy n Save
li_list = ul_new.find_all("li")
news_list = []
for li in li_list:
    a = li.h4.a
    link = url + a["href"]
    title = a.string
    news = {
        "title" : title,
        "link" : link
    }
    news_list.append(news)

# print(news_list)   
pyexcel.save_as(records = news_list, dest_file_name = "dantri.xlsx")



