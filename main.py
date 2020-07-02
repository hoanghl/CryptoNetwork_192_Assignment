
import sys

from bs4 import BeautifulSoup

from checkingModules import check_HoangLe_Abnormal, check_HoangLe_Structure, check_KhoaTran_SizeQuantity

# URL = "http://localhost/"


if __name__ == "__main__":

    ############################
    ## Tải content của file `index.html`
    ############################
    print("= Reading conten file       : ", end='')

    with open('thiswebsite/index.html') as dat_file:
        htmlParser = BeautifulSoup(dat_file.read(), "html.parser")

    print("Done")



    ############################
    ## Tiến hành kiểm tra deface
    ############################
    print("= Checking conditions: ")

    #### Kiểm tra cấu trúc
    if not check_HoangLe_Structure(htmlParser):
        print("==> Defaced by Structure    : Yes")
        sys.exit(0)
    print("==> Defaced by Structure    : No")


    #### Kiểm tra số lượng các tag và số lượng chữ
    if not check_KhoaTran_SizeQuantity(htmlParser):
        print("==> Defaced by Size/Quantity: Yes")
        sys.exit(0)
    print("==> Defaced by Size/Quantity: No")


    #### Kiểm tra màu sắc các thành phần quan trọng
    if not check_HoangLe_Abnormal(htmlParser):
        print("==> Defaced by Color        : Yes")
        sys.exit(0)
    print("==> Defaced by Color        : No")
