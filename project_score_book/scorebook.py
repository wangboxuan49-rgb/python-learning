"""一个表示成绩表的类"""

from student import Student


class Scorebook:
    def __init__(self):
        self.students = []

    def load(self, path):   
        #path是一个传入的实例化的对象，分配一块内存,造出一个新的空对象，
        #自动调用 __init__,把这个新对象作为 self 传进去，返回这个对象,你才能用变量接住
        line_num = 0
        contents = path.read_text() #self.contents改成局部变量 contents, self. 是给"这个对象需要长期记住的东西"用的
        for line in contents.splitlines():
            line_num += 1
            if line.strip() == '':      #判断是否为空行
                continue
            words = line.split()
            name = words[0]
            scores = []
            if len(words) < 2:
                print(f"第 {line_num} 行没有成绩，已跳过：{line}")
                continue
            try:
                for x in words[1:]:
                    scores.append(int(x))
            except ValueError:
                print(f"第 {line_num} 行含非数字成绩，已跳过：{line}")
                continue
            # any(条件 for x in 序列)    # 存在一个满足 → True
            # all(条件 for x in 序列)    # 全部满足   → True
            if any(s < 0 or s > 100 for s in scores):
                print(f"第 {line_num} 行成绩超出 0-100，已跳过：{line}")
                continue
            self.add(Student(name, scores)) #实例化一个 Student 对象，在 self 指向的那个实例上找函数

    def add(self, student):
        self.students.append(student)       #给列表追加一个元素，这个元素是一个实例化对象

    def save(self, path):
        if self.students == []:
            return
        lines = []
        for s in self.students:
            # join 用法： "连接符".join(可迭代对象)，可迭代对象为列表，列表元素必须都是字符串
            #[str(n) for n in [1, 2, 3]]   # 列表推导式 → list，列表推导式返回新列表，可以反复利用
            #str(n) for n in [1, 2, 3]     # 生成器表达式 → generator(没有外面的 [])，生成器只能遍历一次
            score_text = " ".join(str(x)for x in s.student_scores)     #将列表元素拼接成字符串
            lines.append(f"{s.student_name} {score_text}")
        contents = "\n".join(lines)
        path.write_text(contents + '\n')    #文件末尾追加换行

    def report(self):       #函数返回一个报表（字符串）
        # sorted 返回一个新的排好序的列表,原数据不动。
        # key 接收一个函数,sorted 会先对每个元素调用它,按返回值排序,但最终结果里仍然保留原元素。
        # 倒序:reverse=True
        # Student.compute_average 拿到的就是这个函数本尊
        if self.students == []:
            return ""    
        order = sorted(self.students, key = Student.compute_average, reverse = True)
        head = f"{'姓名':<8}{'平均分':>8}{'总分':>8}"
        line = '-' * 24
        score_list = [head, line]
        for o in order:
            score_list.append(f"{o.student_name:<8}{o.compute_average():>8.1f}{o.compute_total():>8}")
        return "\n".join(score_list)