#  功能:最喜欢的书
#  作者:wbx
#  日期:2026-09-24

def favorite_book(title):       #形参，函数完成工作所需的信息
    print(f"One of my favorite books is {title}")

book_name = input("请输入一本书名：")
favorite_book(book_name)        #实参，调用函数时传递给函数的信息