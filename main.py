import argparse

from generator import Generator

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='RRGitH (Resume Repositories GitHub)')

    help_text = "Define the languages that the projects should use, separated by a comma." + \
    "E.g.: Python,HTML"

    parser.add_argument(
        "-l",
        "--languages",
        dest="languages",
        type=str,
        help=help_text,
        default="Python",
    )
    parameters = parser.parse_args()
    languages = parameters.languages.split(",")

    generator = Generator(languages)
    generator.generate_chart()
    generator.generate_csv()