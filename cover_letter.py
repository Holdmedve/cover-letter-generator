import openai
import os
import requests

from io import BytesIO
from pypdf import PdfReader
from bs4 import BeautifulSoup


openai.api = os.getenv("OPENAI_API_KEY")


def extract_cv_text(cv_file):
    cv = PdfReader(BytesIO(cv_file.read()))
    return cv.pages[0].extract_text()


def scrape_linkedin_job_description(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup.find('div', class_='description__text description__text--rich').getText()


def prompt_model_for_cover_letter(job_description, cv):
    prompt = f'write a cover letter for this job: {job_description}. This is my CV: {cv}'
    response = openai.Completion.create(
        model='text-davinci-003', 
        prompt=prompt, 
        max_tokens=512,
        temperature=0.6, 
        n=1, 
    )
    print(response)
    return response['choices'][0]['text']


def generate_cover_letter(cv_file, linkedin_job_url):
    cv = extract_cv_text(cv_file)
    job_description = scrape_linkedin_job_description(linkedin_job_url)
    return prompt_model_for_cover_letter(job_description=job_description, cv=cv)
