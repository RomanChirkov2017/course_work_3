from funktions.funktions import create_list_class

from pathlib import Path


def main():
    file_name = Path(__file__).parent

    list_ex = create_list_class(Path(file_name, 'side_file', 'operations.json'))

    for i in range(5):

        list_ex[i].format_date()
        list_ex[i].choice()
        list_ex[i].beautiful_output()


if __name__ == '__main__':
    main()
