from utils import parse, sort_data, data_json

file_name = 'operations.json'

def main():
    data = data_json(file_name)
    data = sort_data(data)
    data = parse(data)
    print(data)


#
if __name__ == '__main__':
    main()