from os import chmod, environ, path as os_path
from subprocess import call as call_subprocess
from tempfile import NamedTemporaryFile


def generate_pdf(html='', url='', options=[]):
    # Validate input
    if not html and not url:
        raise ValueError('Must pass HTML or specify a URL')
    if html and url:
        raise ValueError('Must pass HTML or specify a URL, not both')

    wkhtmltopdf_default = 'wkhtmltopdf-heroku'

    # Reference command
    wkhtmltopdf_cmd = environ.get('WKHTMLTOPDF_CMD', wkhtmltopdf_default)

    # Set up return file
    pdf_file = NamedTemporaryFile(delete=False, suffix='.pdf')

    if html:
        # Save the HTML to a temp file
        html_file = NamedTemporaryFile(delete=False, suffix='.html')
        html_file.write(bytes(html,'UTF-8'))
        html_file.close()
        url = html_file.name
    
    call_subprocess([wkhtmltopdf_cmd, '-q'] + options + [url, pdf_file.name])

    return pdf_file
