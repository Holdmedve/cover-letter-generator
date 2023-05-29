﻿# cover-letter-generator

Are you tired of writing cover letters to job postings? Then you are in the right place.

This application helps you generate a cover letter based on your resume(cv) and the job posting you would like to apply for. Simply paste the url of the job posting, upload your resume and hit the button! In a few seconds a fully coherent cover letter will be in front of you.

Under the hood this application does 3 things:
- `scrapes` the relevant parts from the job posting based on the provided url
- reads the contents of the resume
- prompts a language model via the `openai API` to write a cover letter based on the cv and job posting

Demo: https://f1e6-2001-4c4e-1e91-4300-d227-88ff-fedd-49f0.ngrok-free.app

This is a link to my `streamlit` application that is exposed to the internet with the help of `ngrok`.

Python version used: 3.7
