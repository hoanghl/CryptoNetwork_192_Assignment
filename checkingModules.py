''' File này sẽ chứa code chính của mọi người
'''

import json

from bs4 import BeautifulSoup


####################
## Đọc file `defaultFootprint.json`
####################
with open('defaultFootprint.json', 'r') as footprint_file:
    footprints = json.load(footprint_file)



def check_KhoaTran_SizeQuantity(htmlParser:BeautifulSoup) -> bool:
    """ Hàm của anh Khoa Trần, sẽ kiểm tra các yếu tố sau:
    - Số lượng tag của website
    - Số lượng chữ trong các tag p

    Args:
        htmlParser (BeautifulSoup): instance của class BeautifulSoup

    Returns:
        bool: True nếu bị defaced, otherwise False
    """
    isDefaced = False

    ## Code goes here..
    ## Anh sẽ đọc số lượng của tag h1 -> h3, tag a, div, số lượng của các ký tự trong tag p 
    ## rồi đối chiếu với các giá trị tương ứng trong file `defaultFootprint.json`

    ## Anh dùng biến `footprints` (lúc này là một dictionary) để truy xuất dữ liệu nhé,
    ## khỏi cần hiện thực code đọc 'defaultFootprint.json'

    return isDefaced


def check_HoangLe_Structure(htmlParser:BeautifulSoup) -> bool:
    """ Hàm của Hoàng Lê, sẽ kiểm tra các yếu tố sau liên quan tới cấu trúc html:

    Args:
        htmlParser (BeautifulSoup): instance của class BeautifulSoup

    Returns:
        bool: True nếu bị defaced, otherwise False
    """

    isDefaced = False

    ## Code goes here..

    return isDefaced

def check_HoangLe_Abnormal(htmlParser:BeautifulSoup) -> bool:
    """ Hàm của Hoàng Lê, sẽ kiểm tra các yếu tố sau liên quan tới CSS:
    - Màu nền
    - Màu h1

    Args:
        htmlParser (BeautifulSoup): instance của class BeautifulSoup

    Returns:
        bool: True nếu bị defaced, otherwise False
    """
    isDefaced = False

    ## Code goes here..

    return isDefaced
