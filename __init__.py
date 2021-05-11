from mycroft import MycroftSkill, intent_file_handler
import os

class DisplayToggle(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('toggle.display.intent')
    def handle_toggle_display(self, message):
        if "on" in message:
            self.speak_dialog('toggle.display')
            os.system("vcgencmd display_power 1")
         else:
            os.system("vcgencmd display_power 0")


def create_skill():
    return DisplayToggle()

