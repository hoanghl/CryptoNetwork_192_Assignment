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
    # isDefaced = False

    ## Code goes here..
    ## Anh sẽ đọc số lượng của tag h1 -> h3, tag a, div, số lượng của các ký tự trong tag p 
    ## rồi đối chiếu với các giá trị tương ứng trong file `defaultFootprint.json`

    ## Anh dùng biến `footprints` (lúc này là một dictionary) để truy xuất dữ liệu nhé,
    ## khỏi cần hiện thực code đọc 'defaultFootprint.json'

    h1_bs = htmlParser.find_all('h1')
    h1_count = len(h1_bs)

    h2_bs = htmlParser.find_all('h2')
    h2_count = len(h2_bs)

    h3_bs = htmlParser.find_all('h3')
    h3_count = len(h3_bs)

    p_bs = htmlParser.find_all('p')
    p_count = len(p_bs)

    a_bs = htmlParser.find_all('a')
    a_count = len(a_bs)

    div_bs = htmlParser.find_all('div')
    div_count = len(div_bs)

    img_bs = htmlParser.find_all('img')
    img_count = len(img_bs)

    article_bs = htmlParser.find_all('article')
    article_count = len(article_bs)

    if (h1_count != footprints['KhoaTran_SizeQuantity']['no_h1']) or (h2_count != footprints['KhoaTran_SizeQuantity']['no_h2']) or (h3_count != footprints['KhoaTran_SizeQuantity']['no_h3']) or (p_count != footprints['KhoaTran_SizeQuantity']['no_p']) or (a_count != footprints['KhoaTran_SizeQuantity']['no_a']) or (div_count != footprints['KhoaTran_SizeQuantity']['no_div']) or (img_count != footprints['KhoaTran_SizeQuantity']['no_img']) or (article_count != footprints['KhoaTran_SizeQuantity']['no_article']):
        return True

    return False



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
