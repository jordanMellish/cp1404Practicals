"""
Sort files based on extension and user categorisation
"""
import os
import shutil


def main():
    extension_to_category = {}
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue
        # Get extension of file
        extension = filename.split('.')[-1]
        if extension not in extension_to_category:
            category = input("What category would you like to sort {} files into? ".format(extension))
            # Now we can map this new extension to a folder name
            extension_to_category[extension] = category
            try:
                # We don't expect to get an exception due to the if statement
                # But we'll play it safe anyway in case the user chooses an existing folder
                os.mkdir(category)
            except FileExistsError:
                pass
        shutil.move(filename, extension_to_category[extension])

main()
