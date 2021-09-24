import requests
import bs4

def any_quotes(soup):
    main_tag = soup.select(".col-md-8")
    if len(main_tag) != 2:
        raise Exception(f"No main tag for the quotes at all!")
    else:
        return len(main_tag[1].select(".quote")) != 0

def get_pages(url):
    page_num = 1
    quotes_present = True
    while quotes_present:
        page = requests.get(f"{url}{page_num}")
        soup = bs4.BeautifulSoup(page.text, "lxml")
        if any_quotes(soup):
            page_num += 1
            yield soup
        else:
            quotes_present = False

def main():
    unique_authors = set()
    for page_soup in get_pages("https://quotes.toscrape.com/page/"):
        for author in page_soup.select(".author"):
            unique_authors.add(author.text)
    print(unique_authors)

if __name__ == "__main__":
    main()
