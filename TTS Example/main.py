from kivy.app import App
from kivy.lang import Builder
from plyer import tts   

KV = """
BoxLayout:
    orientation: "vertical"
    TextInput:
        id: text2say
        text: "Enter your text here"
        font_size:30
    Button:
        text: "Read"
        font_size:30
        size_hint_y:0.2
        on_release:app.readText()
"""

class TextToSpeechApp(App):
    def build(self):
        return Builder.load_string(KV)
    
    def readText(self):
        try:tts.speak(self.root.ids.text2say.text)
        except Exception as e:pass

if __name__ == '__main__':
    TextToSpeechApp().run()