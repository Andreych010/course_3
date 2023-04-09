
from datetime import datetime
import json
import operator

file_name = 'operations.json'
executed = 'EXECUTED'


def output_operations(file_name):
    with open(file_name, encoding='utf-8') as f:
        response_ = f.read()
        response = json.loads(response_)
    return response


def sort_n(respons):
    sort_ = [date for date in respons if 'date' in date]
    sort_.sort(key=operator.itemgetter('date'), reverse=True)
    return sort_


def get_payment_type(payment):
    if 'счет' in payment.lower():
        return f'{payment[:5]}**{payment[-4:]}'
    else:
        payment_type = f'{payment.split()[len(payment.split()) - 1]}'
        card_type = f'{payment.replace(f" {payment_type}", "")}'
        payment_type = payment_type[:-10] + '** **** ' + payment_type[12:]
        payment_type = f'{card_type} {payment_type[:4]} {payment_type[4:]}'
        return payment_type


def parse(res):
    count = 0
    for i in res:
        if count == 5:
            return
        if len(i) > 0 and i['state'] == executed:

            datetime_str = i['date'].split('T')[0]
            datetime_object = datetime.strptime(datetime_str, '%Y-%m-%d').date().strftime('%d.%m.%Y')
            cost = f'{i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}'
            print(f'{datetime_object} {i["description"]}')
            if 'открытие' in i['description'].lower():
                print(f'{get_payment_type(i["to"])}')
            else:
                print(f'{get_payment_type(i["from"])} -> {get_payment_type(i["to"])}')
            print(cost)
            print()
            count += 1

# print(get_payment_type(output_operations(file_name)))
# print(sort_n(output_operations(file_name)))
# print(parse(sort_n(output_operations(file_name))))
#
# print(output_operations(file_name))
