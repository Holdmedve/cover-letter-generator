import openai
import os
import requests

from pypdf import PdfReader
from bs4 import BeautifulSoup

openai.api = os.getenv("OPENAI_API_KEY")

def main():
    cv = PdfReader('botond_talos_cv.pdf')
    number_of_pages = len(cv.pages)
    page = cv.pages[0]
    cv_text = page.extract_text()

    URL = "https://www.linkedin.com/jobs/view/3608802118/?alternateChannel=search&refId=72Guo3os4OXMRrw71tpcbg%3D%3D&trackingId=6oKe455c%2BlwD7NXfx4MRXA%3D%3D"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    job_description = soup.find('div', class_='description__text description__text--rich').getText()
    # print(job_description)

    prompt = f'write a cover letter for this job: {job_description}. This is my CV: {cv_text}'
    response = openai.Completion.create(model='text-davinci-003', prompt=prompt, temperature=0.6, n=1, max_tokens=1000)
    cover_letter = response['choices'][0]['text']
    # print(cover_letter)
    print(response)


if __name__ == '__main__':
    main()
