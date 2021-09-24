import requests
import bs4
from os.path import exists

url = "https://en.wikipedia.org/wiki/Shahar_Marcus"
response_filename = "response_content.txt"
section_delimiter = ">==========<"

def get_content():
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
    print(section_delimiter)
    return response_content

def grab_title_and_paragraphs(soup):
    title_tag = soup.select("title")
    print(f"Title tag of {type(title_tag)} type: {title_tag}")

    paragraph_tags = soup.select("p")
    print(f"Amount of paragraphs in the page: {len(paragraph_tags)}")

    for p_tag in paragraph_tags:
        p = p_tag.get_text().strip(' \n')
        print(f"\t'{p}'")
    print(section_delimiter)
    return title_tag, paragraph_tags

def grab_table_of_content_bullets(soup):
    bullets = soup.select(".toctext")

    for b in bullets:
        print(f"\t'{b.get_text()}'")

    print(section_delimiter)
    return bullets

def grab_images(soup):
    images = soup.select("img")

    print(f"The page contains {len(images)} images as a part of content. Here they are:")

    for i in images:
        print(f"\t{i}")

    jpg_images = [image for image in images if ".jpg" in image['src']]

    print(section_delimiter)
    print(f"The page contains {len(jpg_images)} JPG images. Here they are:")

    for idx, jpg in enumerate(jpg_images):
        print(f"\t{jpg}")
        jpg_path = f"image_{idx}.jpg"

        if not exists(jpg_path):
            jpg_url = "https:" + jpg["src"]
            print(f"\t\tTrying to request the image by this url: {jpg_url}")
            jpg_image_content = requests.get(jpg_url)
            with open(jpg_path, mode="wb") as byte_file:
                byte_file.write(jpg_image_content.content)

        print(f"\t\tJPG image saved at {jpg_path}")

    print(section_delimiter)
    return images

def main():
    response_content = get_content()
    soup = bs4.BeautifulSoup(response_content, "lxml")
    grab_title_and_paragraphs(soup)
    grab_table_of_content_bullets(soup)
    grab_images(soup)



if __name__ == "__main__":
    main()
