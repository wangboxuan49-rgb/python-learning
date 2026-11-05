"""一个表示学生信息的类"""

class Student:
    def __init__(self, student_name, student_scores):
        #给这个对象挂一个叫 student_name 的属性"。之后这个对象身上就带着 student_name 了，不管谁拿着它，都能用 . 取出来
        self.student_name = student_name        
        self.student_scores = student_scores

    def compute_total(self):
        total = 0   #需要初始化累加变量，不会初始置零，会报错
        for score in self.student_scores:
            total += score
        return total

    def compute_average(self):
        if self.student_scores == []:       #没有成绩的情况下
            return 0.0
        average = self.compute_total() / len(self.student_scores)
        return average

    def __str__(self):      #把对象转成字符串
        score_show = '' #需要初始化累加变量，不会初始置零，会报错
        for score in self.student_scores:
            score_show += f" {score}"
        return f"{self.student_name}{score_show}"     #__str__ 必须 return 一个字符串