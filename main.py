import openai
import os
import requests

from pypdf import PdfReader
from bs4 import BeautifulSoup

openai.api = os.getenv("OPENAI_API_KEY")

def extract_cv_text(cv_path):
    cv = PdfReader(cv_path)
    return cv.pages[0].extract_text()


def scrape_linkedin_job_description(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup.find('div', class_='description__text description__text--rich').getText()


def generate_cover_letter(job_description, cv):
    prompt = f'write a cover letter for this job: {job_description}. This is my CV: {cv}'
    response = openai.Completion.create(
        model='text-davinci-003', 
        prompt=prompt, 
        max_tokens=1000,
        temperature=0.6, 
        n=1, 
    )
    return response['choices'][0]['text']


def main():
    cv = extract_cv_text(cv_path='botond_talos_cv.pdf')
    job_description = scrape_linkedin_job_description(
        url="https://www.linkedin.com/jobs/view/3608802118/?alternateChannel=search&refId=72Guo3os4OXMRrw71tpcbg%3D%3D&trackingId=6oKe455c%2BlwD7NXfx4MRXA%3D%3D"
    )
    cover_letter = generate_cover_letter(job_description=job_description, cv=cv)
    print(cover_letter)
    
    


if __name__ == '__main__':
    main()
