import requests
import bs4

links = []

url = 'https://www.tradebit.com/filesharing.php/1005-Documents-eBooks-Educational'

page = requests.get(url)
# print(page.content)
soup = bs4.BeautifulSoup(page.content, "html.parser")
# book=[b.get_text().strip() for b  in soup.find_all('div',{'class':'post-title'})]


urlinkbase = soup.select('center ul  a')
book = soup.find_all('div', {'class': 'post-title'})
bookdescs = soup.find_all('div', {'style': 'line-height: 1.4em; font-size: 1.2em;'})
bookpricc = soup.find_all('div', {'style': 'padding-top: 5px; font-size: 12px; height:25px;'})
books = [b.get_text().strip() for b in book]
bookdescrip = [b.get_text().strip() for b in bookdescs]
bookpri = [b.get_text().strip() for b in bookpricc]
print(f"""
===========================

     book name is

==========================

{books}
============================

       book descriptins is 

============================
""")
print(f"""{bookdescrip}
=============================

        book price  is 

============================
""")
print(f"""{bookpri}
=============================

       boook name is

==============================
""")

for i in range(len(urlinkbase)):
    links.append(urlinkbase[i].get_attribute_list('href'))

for link in links:
    session1 = requests.session()
    result = session1.get(link[0])
    soupp = bs4.BeautifulSoup(result.content, "html.parser")
    bookname = soupp.find_all('div', {'class': 'post-title'})
    bookdescription = soupp.find_all('div', {'style': 'line-height: 1.4em; font-size: 1.2em;'})
    bookprice = soupp.find_all('div', {'style': 'padding-top: 5px; font-size: 12px; height:25px;'})

    booknam = [bn.get_text().strip() for bn in bookname]
    print(f""""{booknam}

 =============================

       book descriptins is 

 ==============================

""")
    bookdesc = [bn.get_text().strip() for bn in bookdescription]
    print(f""""{bookdesc}
   ============================

           book  price     is 

   ============================

  """)
    bookpric = [bn.get_text().strip() for bn in bookprice]

    print(f"""{bookpric}

 ============================

         book   name  is

============================

""")
