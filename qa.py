import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
#add headers to avoid access denied
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
r= requests.get("https://machinelearninginterview.com/natural-language-processing-interview-questions/")
c= r.content
#Use beatifulsoup to parse
soup = BeautifulSoup(c, "html.parser")
#content in dictinary
nlp={"Questions":[], "Answers":[]}
lis=soup.find_all("li")
for li in lis:
    q=li.find("a").get("title")
    if q!=None:
        nlp["Questions"].append(q)

div= soup.find_all("div", {"class":"lcp_excerpt"})
for a in div:
    if a!=None:
        nlp["Answers"].append(a.text)
#save dictionary to dataframe
df=pd.DataFrame(nlp)
df.to_csv("nlpqa.csv")
print("data saved to csv")

