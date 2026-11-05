#  功能:成绩记录程序
#  作者:wbx
#  日期:2026-10-06

from pathlib import Path
from student import Student
from scorebook import Scorebook


def main():
    score_book = Scorebook()
    path = Path('scores.txt')
    try:
        score_book.load(path)       #启动时把磁盘上的记录装进内存
        print(f"已从{path}中读取到了{len(score_book.students)}条记录")
    except FileNotFoundError:
        print("暂无记录，已新建成绩册")
    
    while True:
        print()
        print('1.录入学生\n2.显示报表\n3.保存退出')
        choice = input('请输入：').strip()

        if choice == '1':
            name = input('请输入学生姓名：').strip()
            if name == "":
                break
            scores = []
            score_contents = input('请输入学生成绩（用空格分隔）：')
            for score in score_contents.split():
                scores.append(int(score))
            student = Student(name, scores)
            score_book.add(student)
            print(f"已添加 {student.student_name}")

        elif choice == '2':
            if score_book.report() == '':
                print('无记录')
            else:
                print(f'{score_book.report()}')

        elif choice == '3':
            break
        
        else:
            print("没有这个选项，请输入 1、2 或 3")

    score_book.save(path)
    print(f"已保存到 {path}，程序结束")

if __name__ == "__main__":
    main()