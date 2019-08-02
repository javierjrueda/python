>>> import requests
>>> # Make sure that your key is in the URL
>>> ifttt_webhook_url = 'https://maker.ifttt.com/trigger/test_event/with/key/{your-IFTTT-key}'
>>> requests.post(ifttt_webhook_url)
<Response [200]>