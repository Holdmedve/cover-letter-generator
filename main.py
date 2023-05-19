from pypdf import PdfReader
import requests
from bs4 import BeautifulSoup

def main():
    reader = PdfReader('botond_talos_cv.pdf')
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()

    URL = "https://www.linkedin.com/jobs/view/3608802118/?alternateChannel=search&refId=72Guo3os4OXMRrw71tpcbg%3D%3D&trackingId=6oKe455c%2BlwD7NXfx4MRXA%3D%3D"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    job_description = soup.find('div', class_='description__text description__text--rich').getText()
    print(job_description)

if __name__ == '__main__':
    main()
