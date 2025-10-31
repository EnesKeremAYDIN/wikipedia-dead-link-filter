import requests
from bs4 import BeautifulSoup
import logging
import time

logging.basicConfig(filename='bot.log', level=logging.INFO)

def fetch_links(url, limit, keyword=None):
    links = []
    count = 0
    page_number = 1
    while url and (limit == 0 or count < limit):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        for li in soup.find_all('li'):
            a_tag = li.find('a')
            if a_tag and 'href' in a_tag.attrs:
                title = a_tag.get('title')
                link = 'https://en.wikipedia.org' + a_tag.get('href')
                links.append((title, link))
        
        save_links(links, 'links.txt')
        
        if keyword:
            filtered_links = filter_links(links, keyword)
            save_links(filtered_links, 'filter.txt')
        
        next_page = soup.find('a', string="next page")
        if next_page and 'href' in next_page.attrs:
            url = 'https://en.wikipedia.org' + next_page.get('href')
            logging.info(f"Page {page_number}: {url}")
            print(f"Page {page_number}")
            count += 1
            page_number += 1
            time.sleep(2)
        else:
            url = None

    return links

def save_links(links, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for title, link in links:
            f.write(f"[{title}]({link})\n")
            logging.info(f"Saved link: {title} - {link}")

def filter_links(links, keyword):
    filtered = [(title, link) for title, link in links if title and keyword.lower() in title.lower()]
    return filtered

def main():
    url = "https://en.wikipedia.org/wiki/Category:Articles_with_dead_external_links"
    filter_option = input("Do you want to filter? (yes-no): ").strip().lower()
    keyword = None
    if filter_option == 'yes':
        keyword = input("Enter the filter keyword: ").strip()
    
    limit = int(input("Enter the number of pages to scan (0 = unlimited): "))
    links = fetch_links(url, limit, keyword)
    
    logging.info("Bot operation completed.")
    print("Operation completed.")

if __name__ == "__main__":
    main()
