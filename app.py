
import os
import webview
import requests

class Api:
    def getData(self,place):
        

        api_key = "YOUR API KEY"

        city = place

      
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        response = requests.get(url)

        if response.status_code == 200:
            return response.json()


if __name__ == '__main__':
    api = Api()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    html_file = os.path.join(current_dir, 'index.html')
    window = webview.create_window('My Desktop App', html_file, js_api=api)
    webview.start()