from bs4 import BeautifulSoup
import requests
import pandas as pd
import json


def get_html(url):
    response = requests.get(url)
    return response.text

def get_quotes():
    datas = []
    total_pages = 10

    for i in range (1, total_pages+1):  # loop sampe 10 hal
        url = f"https://quotes.toscrape.com/page/{i}/"
        print(f"fetching page {i}of {total_pages}") #ini untuk ngecek udah sampe page brp
        print(i/total_pages * 100, f"% downloading") #ini untuk nge print percentase udah berapa persen dri data yg lagi di print
    
        html = get_html(url)
        soup = BeautifulSoup(html, 'html.parser')
        element = soup.find_all("div", class_ ="quote")
        for quote in element:
            text = quote.find("span", class_="text")
            author = quote.find("small", class_="author")
            # print(text.text)
            # print(author.get_text())

            quotes = {"quote": text.text, "author": author.text}
            datas.append(quotes)  

    # with open("quotes.json", "w") as file: 
    #     json.dump(datas, file) 
    #     convert = pd.DataFrame(datas)
    #     convert.to_excel("quotes.xlsx", index=False)
    #     print(datas)
    print(datas)
    return datas
       

if __name__ == "__main__":
    get_quotes()
    print("Quotes have been saved to quotes.json and quotes.xlsx")
    