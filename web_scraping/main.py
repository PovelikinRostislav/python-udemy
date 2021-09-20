import requests
import bs4
from os.path import exists

url = "https://en.wikipedia.org/wiki/Shahar_Marcus"
response_filename = "response_content.txt"

def main():
    if not exists(response_filename):
        print(f"Sending a request to get the page: {url}")
        response = requests.get(url)
        with open(response_filename, mode="w") as file:
            file.writelines(response.text)
        response_content = response.text
    else:
        print(f"Reading the response content from the file: {response_filename}")
        with open(response_filename, mode="r") as file:
            response_content = file.readlines()
            response_content = "\n".join(response_content)

    print(f"Response content type: {type(response_content)}")

    soup = bs4.BeautifulSoup(response_content, "lxml")
    title_tag = soup.select("title")
    print(f"Title tag of {type(title_tag)} type: {title_tag}")

    paragraph_tags = soup.select("p")
    print(f"Amount of paragraphs in the page: {len(paragraph_tags)}")

    for p_tag in paragraph_tags:
        p = p_tag.get_text().strip(' \n')
        print(f"\t'{p}'")



if __name__ == "__main__":
    main()
