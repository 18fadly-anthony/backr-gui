from gooey import Gooey, GooeyParser

@Gooey(target="backr.py -w")

def main():
    parser = GooeyParser()
    backr = parser.add_argument_group()
    backr.add_argument('-s',
                       metavar="Choose folder to backup",
                       widget="DirChooser",
                       required=True
    )
    backr.add_argument('-l',
                       metavar="Choose folder to store backup",
                       widget="DirChooser",
                       required=True
    )
    backr.add_mutually_exclusive_group(
        gooey_options={
            backr.add_argument('-n',
                               metavar="Do not use compression",
                               widget='BlockCheckbox'
            ),
            backr.add_argument('-c',
                               metavar="Use compression",
                               widget='BlockCheckbox'
            )
        }
    )

    parser.parse_args()

if __name__ == '__main__':
    main()
