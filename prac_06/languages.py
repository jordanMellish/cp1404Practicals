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

languages.append(ruby)
languages.append(python)
languages.append(visual_basic)

# Loop for printing dynamic languages.
print("The dynamically typed languages are")
for language in languages:
    if language.is_dynamic():
        print(language.name)
