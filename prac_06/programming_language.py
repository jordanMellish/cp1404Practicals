class ProgrammingLanguage:
    def __init__(self, language, dynamic, reflection, year):
        self.language = language
        self.dynamic = dynamic.title()
        self.reflection = reflection
        self.year = int(year)

    def __str__(self):
        return "{} , {} Typing, Reflection={}, First appeared in {}".format(self.language, self.dynamic,
                                                                           self.reflection, self.year)

    def is_dynamic(self):
        if self.dynamic == "Dynamic":
            return True
        else:
            return False
