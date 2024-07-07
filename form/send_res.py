import os
import requests
from requests.structures import CaseInsensitiveDict
import os
from dotenv import load_dotenv

def send_res(form):
    load_dotenv()

    sendgrid_api_key = os.getenv('API_KEY')

    url = "https://api.sendgrid.com/v3/mail/send"

    headers = CaseInsensitiveDict()
    headers["Authorization"] = f"Bearer {sendgrid_api_key}"
    headers["Content-Type"] = "application/json"

    data = {
    "personalizations": [
        {
        "to": [
            {
            "email": "dramsgard@gmail.com"
            }
        ],
        "subject": "Patient Forms",
        }
    ],
    "from": {
        "email": "dramsgard@gmail.com",
    },
    "content": [
        {
        "type": "text/plain",
        "value": f"Dear Dr. Aspenleiter,\n\nYou have one new request for consultation. The following attached form has all the detials regarding patient information.",
        }
    ],
    "attachments": [
            {
                "content": form,
                "filename": "form.pdf",
                "type": "application/pdf",
                "disposition": "attachment"
            }
        ]
    }

    requests.post(url, headers=headers, json=data)