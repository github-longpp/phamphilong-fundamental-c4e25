from urllib.request import urlopen 
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

conn = urlopen(url)

raw_data = conn.read()

content = raw_data.decode("utf8")

soup = BeautifulSoup(content, "html.parser")
table = soup.find("table",id="tableContent")
tr_list = table.find_all("tr")

rp = []
for tr in tr_list:
    td_list = tr.find_all("td", "b_r_c")
    for td in td_list:
        td = td.string 
        content = {
           " ":td
        }
        print(td)
        rp.append(content)

pyexcel.save_as(records=rp, dest_file_name="ex2.xlsx")