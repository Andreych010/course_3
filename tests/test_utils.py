
from utils import sort_n
def test_sort_n(test_data):
    sort_nt = sort_n(test_data)
    for v in sort_nt:

        print(v['data'])
    #assert utils.sort_n(test_data) ==
