"""
CP1404/CP5632 Practical
Cleaning up files
"""
import os


def main():
    """Cleanup inconsistent song lyrics file names."""

    # Change to desired directory
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):

        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))

            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, new_name)
            os.rename(full_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    # No solution is provided, but you may want to consider the patterns to look out for and fix
    # E.g. a lowercase letter followed by a capital, like "tN" should become "t_N"
    # Try doing this on paper first and then see if you can systematise it
    formatted_name = ""
    for i, letter in enumerate(filename):
        if filename[i].islower() and filename[i + 1].isupper():
            formatted_name += "{}_".format(letter)
        else:
            formatted_name += letter
    new_name = formatted_name.replace("TXT", "txt")
    return new_name


main()
