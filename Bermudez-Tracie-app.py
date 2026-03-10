# Tracie Bermudez (w10214815)

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class TipApp(App):
    def build(self):
        primary_layout = BoxLayout(orientation="vertical")
        primary_layout.padding = (25, 25, 25, 25)
        primary_layout.spacing = 15 
        
        lblTitle = Label(text="Tip Calculator")
        lblTitle.font_size = "40sp"
        
        self.txtSubTotal = TextInput()
        self.txtSubTotal.hint_text = "Sub-Total..."
        self.txtSubTotal.font_size = "30sp"
        self.txtSubTotal.bind(text=self.subtotal_text_changed)
        
        tip15Prompt = Label(text="15%")
        tip15Arrow = Label(text="->")
        self.tip15Output = Label(text="$")
        self.tip15Output.font_size = "35sp"

        layout15 = BoxLayout(orientation="horizontal")
        layout15.add_widget(tip15Prompt)
        layout15.add_widget(tip15Arrow)
        layout15.add_widget(self.tip15Output)
        
        tip20Prompt = Label(text="20%")
        tip20Arrow = Label(text="->")
        self.tip20Output = Label(text="$")
        self.tip20Output.font_size = "35sp"

        layout20 = BoxLayout(orientation="horizontal")
        layout20.add_widget(tip20Prompt)
        layout20.add_widget(tip20Arrow)
        layout20.add_widget(self.tip20Output)
        
        tip25Prompt = Label(text="25%")
        tip25Arrow = Label(text="->")
        self.tip25Output = Label(text="$")
        self.tip25Output.font_size = "35sp"

        layout25 = BoxLayout(orientation="horizontal")
        layout25.add_widget(tip25Prompt)
        layout25.add_widget(tip25Arrow)
        layout25.add_widget(self.tip25Output)

        primary_layout.add_widget(lblTitle)
        primary_layout.add_widget(self.txtSubTotal)
        primary_layout.add_widget(layout15)
        primary_layout.add_widget(layout20)
        primary_layout.add_widget(layout25)

        return primary_layout
    
    # Event Method Tracie Bermudez (w10214815)
    def subtotal_text_changed(self, instance, value):
        try:
            subtotal = float(self.txtSubTotal.text)
        except ValueError:
            self.tip15Output.text = "$"
            self.tip20Output.text = "$"
            self.tip25Output.text = "$"
            return

        tip15 = subtotal * 0.15
        tip20 = subtotal * 0.20
        tip25 = subtotal * 0.25

        self.tip15Output.text = f"${tip15:.2f}"
        self.tip20Output.text = f"${tip20:.2f}"
        self.tip25Output.text = f"${tip25:.2f}"

if __name__ == "__main__":
    app = TipApp()
    app.run()