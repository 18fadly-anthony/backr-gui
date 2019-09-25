import os
from gooey import Gooey, GooeyParser

@Gooey(target="backr.py -n -w")

def main():
    parser = GooeyParser()
    backr = parser.add_argument_group()
    backr.add_argument('-s',
                       metavar="Choose folder to backup",
                       widget="DirChooser",
    )
    backr.add_argument('-l',
                       metavar="Choose folder to store backup",
                       widget="DirChooser",
    )

    parser.parse_args()

if __name__ == '__main__':
    main()
