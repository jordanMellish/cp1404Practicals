from prac_06.programming_language import ProgrammingLanguage

languages = []

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print(ruby)
print(python)
print(visual_basic)

print(ruby.is_dynamic())
print(python.is_dynamic())
print(visual_basic.is_dynamic())

languages.append(str(ruby))
languages.append(str(python))
languages.append(str(visual_basic))
print(languages)

dynamic_languages = []
for language in languages:
    language = language.split()
    if language[1] == "Dynamic":
        dynamic_languages.append(language[0])
print(dynamic_languages)