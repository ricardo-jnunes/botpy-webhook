import json
import requests
from bs4 import BeautifulSoup as bs

def extract_data(content):
    bs_content = bs(content, "html.parser")
    scripts = bs_content.find_all('script')
    token = None
    for s in scripts:
        if 'window.sessionStorage.setItem("dt-xsrfToken", "' in s.text:
            script = s.text
            script = script.split('window.sessionStorage.setItem("dt-xsrfToken", "')[1]
            script = script.split('window.sessionStorage.setItem("dt-xsrfToken", "')[0]
            token = script.split('");')[0]
            break

    return token

def highest_thread(response):
    highest_thread = 0
    j = json.loads(response)
    chartDataEntries =  j['chartDataEntries']
    for entries in chartDataEntries:
        dataPoints = entries['dataPoints']
        for dataPoint in dataPoints:
            value = dataPoint['value']
            if value > highest_thread:
                highest_thread = value
    return highest_thread

def get_environment_data():
    
        # Use 'with' to ensure the session context is closed after use.
        # Do login with form submission
        with requests.Session() as s:
            login = s.get("https://dynatrace.xxxxxx.com.br/login")
            bs_content = bs(login.content, "html.parser")
            token = bs_content.find("input", {"name":"X-XSRF-Header"})["value"]
            payload = {
                'username': 'XXXXXXX',
                'password': 'XXXXXXXX',
                'X-XSRF-Header': token
            }

            # Get response and search for xsrfToken, it is necessary due security reasons of plataform that we accessing
            p = s.post('https://dynatrace.xxxxxx.com.br/login', data=payload)
            token = extract_data(p.content)

            # With a valid session, we get the dashboards of dynatrace that we want
            # Use the payload received from Dynatrace to build the dashboard
            payloadmon1 = {}
            payloadmon2 = {}
            r1 = s.post('https://dynatrace.xxxxxx.com.br/rest/charts?sessionid=live-xxxxxx&timeframe=Offset_1_HOURS&resolution=CHART_RESOLUTION_1MIN&limit=41', data=json.dumps(payloadmon1),headers={"Content-Type": "application/json","X-XSRF-Header": token})
            r2 = s.post('https://dynatrace.xxxxxx.com.br/rest/charts?sessionid=live-xxxxxx&timeframe=Offset_1_HOURS&resolution=CHART_RESOLUTION_1MIN&limit=41', data=json.dumps(payloadmon2),headers={"Content-Type": "application/json","X-XSRF-Header": token})
            return 'APP 1: {} e no APP 2: {}'.format(highest_thread(r1.content), highest_thread(r2.content))
    
