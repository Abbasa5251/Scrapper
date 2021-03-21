import requests
import time
import pandas as pd
from requests_html import HTML

def cleaned_data(text, keyname=None):
    if keyname == 'votes':
        return text.replace('\nvotes', '')
    return text

def parse_tagged_page(html):
    question_summaries = html.find(".question-summary")
    keynames = ['question', 'votes', 'tags']
    classes = ['.question-hyperlink', '.vote', '.tags']
    datas = []
    for question_element in question_summaries:
        question_data = {}
        for i, _class in enumerate(classes):
            sub_question_element = question_element.find(_class, first=True)
            keyname = keynames[i]
            question_data[keyname] = cleaned_data(sub_question_element.text, keyname=keyname)
        datas.append(question_data)
    return datas

def extract_url_data(url):
    r = requests.get(url)
    if r.status_code not in range(200,299):
        return []
    html_str = r.text
    html = HTML(html=html_str)
    datas = parse_tagged_page(html)
    return datas

def scrape_tag(tag='python', query_filter="Votes", max_pages=50, page_size=25):
    base_url = "https://stackoverflow.com/questions/tagged"
    datas = []
    for p in range(1,max_pages+1):
        page_num = p
        url = f"{base_url}/{tag}?tab={query_filter}&page={page_num}&pagesize={page_size}"
        datas += extract_url_data(url)
        time.sleep(2)
    return datas

scraped_data = scrape_tag(max_pages=3, page_size=5)
print(scraped_data)
