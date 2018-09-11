class ProgrammingLanguage:
    def __init__(self, name, dynamic, reflection, year):
        self.name = name
        self.dynamic = dynamic.title()
        self.reflection = reflection
        self.year = int(year)

    def __str__(self):
        return "{} , {} Typing, Reflection={}, First appeared in {}".format(self.name, self.dynamic,
                                                                            self.reflection, self.year)

    def is_dynamic(self):
        return self.dynamic == "Dynamic"
