from mycroft import MycroftSkill, intent_file_handler


class DisplayToggle(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('toggle.display.intent')
    def handle_toggle_display(self, message):
        self.speak_dialog('toggle.display')


def create_skill():
    return DisplayToggle()

