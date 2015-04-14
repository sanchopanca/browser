from kivy.app import App
from kivy.uix.label import Label

import requests


class Page(Label):
    pass


class BrowserApp(App):
    def build(self):
        text = requests.get('https://google.com').text
        print(text)
        page = Page(text=text, text_size=(800, None))
        return page


if __name__ == '__main__':
    BrowserApp().run()