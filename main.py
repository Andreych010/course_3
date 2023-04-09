from utils import parse, sort_n, output_operations

file_name = 'operations.json'

def main():
    print(parse(sort_n(output_operations(file_name))))


if __name__ == '__main__':
    main()