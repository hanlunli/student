
import requests
from bs4 import BeautifulSoup
 
 
r = requests.get('https://www.goodreads.com/list/show/2681.Time_Magazine_s_All_Time_100_Novels')
 
soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find('table', class_="tableList js-dataTooltip")
author_unsorted = s.find_all('a', class_="authorName")

authorname=[]
for i in author_unsorted:
    author = i.get_text()
    authorname.append(author.strip())


title_unsorted = s.find_all('a', class_="bookTitle")
titles=[]
for i in title_unsorted:
    title = i.get_text()
    titles.append(title.strip())

spans = s.find_all('span', class_="greyText smallText uitext")
digits_as_strings = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

ratings=[]
numratings = []
for i in spans:
    temp =''
    rating = i.get_text()
    if rating[2] in digits_as_strings:
        ratings.append(float(rating[2:6].strip()))
        # print(rating[19::])
        # print(rating[25::])
        for j in rating[7::].strip():
            # print(j)
            if j in digits_as_strings:
                temp += j
        # print(temp)
        numratings.append(temp)
    elif rating[17] in digits_as_strings:
        ratings.append(float(rating[17:21].strip()))
        for j in rating[22::].strip(): 
            if str(j) in digits_as_strings:
                temp += j
            # print(temp)
        numratings.append(temp)
print(len(ratings)-len(numratings))
print(numratings)
for i in range(len(ratings)):
    emoji = ""
    if ratings[i] >= 4:
        emoji += '❤'
    elif ratings[i] >= 3:
        emoji += '👍'
    else:
        emoji += '👎'
    print(titles[i], "by: ", authorname[i], "with a rating of: ", ratings[i], emoji, "with", numratings[i], "ratings")