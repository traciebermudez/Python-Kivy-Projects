import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from random import randint

Window.size = (600, 320)

class NumberGameApp(App):
    def build(self):
        self._number = randint(0, 100)
        self._guessed = False

        layout = BoxLayout(orientation="vertical",
                           spacing=20,
                           padding=(20, 20, 20, 20))

        lblTitle = Label(text="Guess My Number", font_size="40px")
        layout.add_widget(lblTitle)

        self.txtNumInput = TextInput(
            hint_text="Enter Number", 
            font_size="20px",
            size_hint=(None, None),
            width='400dp',
            height='50dp',
            pos_hint={'center_x': 0.5})
        layout.add_widget(self.txtNumInput)

        self.btnSubmitNumber = Button(
    text="Submit",
    font_size="20px",
    size_hint=(None, None),
    width='200dp',
    height='50dp',
    pos_hint={'center_x': 0.5},
    background_normal='',
    background_color=(0.1, 0.5, 0.9, 1)
)
        self.btnSubmitNumber.bind(on_press=self.submit_clicked)  # <-- this needs submit_clicked to exist
        layout.add_widget(self.btnSubmitNumber)

        self.lblResult = Label(text="Enter a number above", font_size="20px")
        layout.add_widget(self.lblResult)

        return layout

    def submit_clicked(self, instance):
        if not self._guessed:
            try:
                num_input = int(self.txtNumInput.text)
            except ValueError:
                self.lblResult.text = "Error: Not a valid number"
                return

            if num_input == self._number:
                self.lblResult.text = "You guessed it!"
                self.btnSubmitNumber.text = "New Number"
                self._guessed = True
            elif num_input < self._number:
                self.lblResult.text = "Guess a higher number"
            else:
                self.lblResult.text = "Guess a lower number"

        else:
            self._number = randint(0, 100)
            self._guessed = False
            self.txtNumInput.text = ""
            self.lblResult.text = "Enter a number above"
            self.btnSubmitNumber.text = "Submit"

if __name__ == "__main__":
    NumberGameApp().run()