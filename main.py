import streamlit as st

from cover_letter import generate_cover_letter
from input_validation import is_form_incomplete, is_url_invalid


def main():
    with st.form(key='cover-letter-form'):
        linkedin_job_url = st.text_input("LinkedIn Job url")
        cv_file = st.file_uploader("Your CV in PDF format", type="pdf")
        submit_button = st.form_submit_button(label='Submit')
        container = st.container()
    
    if submit_button:
        if is_form_incomplete(file=cv_file, url=linkedin_job_url):
            st.warning('Form is incomplete.')
            return

        if is_url_invalid(url=linkedin_job_url):
            st.warning('Provided url is invalid')
            return

        result = generate_cover_letter(cv_file=cv_file, linkedin_job_url=linkedin_job_url)
        with container:
            st.header('Your cover letter:')
            st.write(result)    


if __name__ == '__main__':
    main()
