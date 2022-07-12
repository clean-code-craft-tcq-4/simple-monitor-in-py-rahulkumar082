class Language:
    def language_switcher(self, required_language, str):
        switcher = {}
        if (required_language == 'German'):
            switcher = {
                "Warning: Approaching charge-peak": "Warnung: Ladespitze nähert sich",
                "Warning: Approaching Discharge": "Warnung: Annäherung an Entladung",
                "Temperature is out of range!": "Temperatur außerhalb des zulässigen Bereichs!",
                "Charge rate is out of range!": "Der Ladestrom liegt außerhalb des zulässigen Bereichs!",
                "State of Charge is out of range!": "Ladezustand außerhalb des Bereichs!"
            }
            return switcher.get(str, "Cannot detect the language")
        return str

    def print_msg_in_language(self, required_language, str, warning_or_error=True):
        updated_str = str
        if (warning_or_error):
            updated_str = self.language_switcher(required_language, str)
        print(f"{self.__class__.__name__}: {updated_str}")
