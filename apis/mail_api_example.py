# Don't forget to "pip install requests"
# Could be "sudo pip install requests"
import requests

# You should be able to get this here: https://app.mailgun.com/app/dashboard
sender = "chris" # Sender is the name it will come from like chris@jeganathan.co.uk
domain_name = "jeganathan.co.uk"
api_key = "YOUR_API_KEY" #Use your own key here


def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/{0}/messages".format(domain_name),
        auth=("api", api_key),
        data={
            "from": "Chris Jeganathan <{0}@{1}>".format(sender, domain_name),
            "to": ["some.email@address.com"],
            "subject": "Test",
            "text": "testing mail"
        }
    )


response = send_simple_message()


print response.url
print response.status_code
print response.headers["content-type"]
print response.text