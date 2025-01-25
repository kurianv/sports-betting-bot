import requests

api_key = '2163ca65881f43c3aaabe8c11362c0ca'
category = input("Enter the category: ")
date = input("Enter the specific date to be searched on (YYYY-MM-DD): ")
news_data = requests.get(f'https://newsapi.org/v2/everything?q={category}&from={date}&sortBy=popularity&apiKey={api_key}')

articles = news_data.json().get('articles', [])

for i in range(len(articles)):
    print(f"{i+1}. {news_data.json()['articles'][i]['title']}") #title
    print(f"By {news_data.json()['articles'][i]['author']}, {news_data.json()['articles'][i]['source']['name']}\n") #source
    
