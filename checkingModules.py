''' File này sẽ chứa code chính của mọi người
'''

import json
import re

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
    def construct(parser:BeautifulSoup) -> list:
        """ Xây dựng cấu trúc cho phần tử được truyền vào

        Args:
            parser (BeautifulSoup): 

        Returns:
            list: list các element
        """
        structure = []
        for x in parser:
            if isinstance(x, str):
                continue

            if len(list(x.children)) > 0:
                tmp = construct(x.children)
                if len(tmp) > 0:
                    structure.append([x.name, tmp])
                else:
                    structure.append(x.name)
            else:
                structure.append(x.name)

        return structure


    for structure in footprints['HoangLe_Structure']:
        tmp = htmlParser.find(structure['tag'], id=structure['id'])
        if tmp is None:
            return True

        series = str(construct(tmp))

        if series != structure['series']:
            return True

    return False



def check_HoangLe_Abnormal(htmlParser:BeautifulSoup) -> bool:
    """ Hàm của Hoàng Lê, sẽ kiểm tra các yếu tố sau liên quan tới CSS:
    - Màu nền
    - Màu h1

    Args:
        htmlParser (BeautifulSoup): instance của class BeautifulSoup

    Returns:
        bool: True nếu bị defaced, otherwise False
    """
    ########################
    ## Kiểm tra điều kiện màu nền chuyển đen
    ########################
    reStr_1 = r" \{([^}]*)\}"

    css_contents = str(htmlParser)

    css_attribute = re.findall("{}{}".format(footprints['HoangLe_Abnormal'][0]['tag'], reStr_1), css_contents)
    if len(css_attribute) == 0:
        return False

    tmp = footprints['HoangLe_Abnormal'][0]['attribute'].replace('(', '\(').replace(')', '\)')

    result = re.findall(tmp, css_attribute[0])

    if len(result) > 0:
        return True

    return False
