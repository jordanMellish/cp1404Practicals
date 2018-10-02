from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicWidgetsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""

    def build(self):
        """
        Build the Kivy GUI.
        :return: reference to the root Kivy widget
        """
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_widgets.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """
        Create buttons from dictionary entries and add them to the GUI
        :return: None
        """
        phonebook = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}

        for name in phonebook:
            # # create a button for each phonebook entry, specifying the text and id
            # # (although text and id are the same in this case, you should see how this works)
            temp_label = Label(text=name)
            # # add the button to the "entries_box" using add_widget()
            self.root.ids.entries_box.add_widget(temp_label)


DynamicWidgetsApp().run()
