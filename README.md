# python-learning

《Python 编程：从入门到实践（第 3 版）》第一部分逐章练习，加上三个可运行的小项目和一组算法题。

练的重点不是把语法过一遍，而是能独立写出“读文件 → 处理数据 → 持久化 → 有测试”的完整脚本：用 `pathlib` 处理文件，用 `try/except` 区分失败原因，用类和模块组织代码，用 `pytest` 验证行为。

## 进度

| 章节 | 主题 | 状态 |
|---|---|---|
| ch01 / ch02 | 起步、变量与简单数据类型 | 完成 |
| ch03 / ch04 | 列表、操作列表 | 完成 |
| ch05 / ch06 | if 语句、字典 | 完成 |
| ch07 | 用户输入与 while 循环 | 完成 |
| ch08 | 函数、模块导入 | 完成 |
| ch09 | 类、继承 | 完成 |
| ch10 | 文件和异常 | 完成 |
| ch11 | 测试代码（pytest） | 完成 |
| ch12 起 | 教材项目部分 | 未开始 |

## 能做什么

- 数据组织：列表、字典、集合、元组；`sorted(key=..., reverse=True)` 做多条件排序，`" ".join(...)` 拼接
- 文件处理：`pathlib.Path.read_text / write_text` 读写文本，`json` 读写结构化数据，区分相对路径与绝对路径
- 错误处理：`try / except / else`，把 `FileNotFoundError`、`ValueError`、数据越界分开处理；逐行校验时报出行号并跳过坏数据
- 函数与模块：位置参数、关键字参数、默认参数、`*args`；一个文件一个模块，导入方向清晰，不做循环导入
- 面向对象：封装、继承、组合，`super()` 初始化父类，`__str__` 控制打印格式
- 测试：`pytest` + `assert`，用 `@pytest.fixture` 共享测试对象，测试与实现分文件
- 算法：双指针、哈希表计数、字典 `.get(key, 0)` 累加

## 项目

### 成绩记录程序（`project_score_book/`）

启动时从 `scores.txt` 载入历史记录，菜单循环完成录入、报表、保存退出，报表按平均分从高到低输出。

- 分三个文件：`student.py`（`Student`：姓名、成绩列表、总分、平均分）、`scorebook.py`（`Scorebook`：添加记录、读写文件、生成报表）、`score_book.py`（菜单与程序入口）
- `Scorebook` 与 `Student` 是组合关系，不是继承
- 读文件时处理四类情况：文件不存在（首次运行，新建成绩册）、行内有非数字（`ValueError`，报行号跳过）、成绩不在 0–100（`any()` 检查，跳过）、只有姓名没有成绩（提示后跳过）；每处跳过后都 `continue`，坏行不会混进成绩册
- 报表用 `sorted(key=Student.compute_average, reverse=True)` 排序，表头和数据列宽对齐

运行：

```sh
cd project_score_book
python3 score_book.py
```

### 词频统计（`ch10/word_report.py`）

读入一个文本文件，输出总行数、非空行数、总单词数、出现次数最多的 3 个单词，结果写入 `report.txt`。

实现要点：`splitlines()` 按行切分、`split()` 按空白切词，统一转小写并去掉常见标点；统计用“单词 + 次数”两个平行列表；排序时把次数取负、与单词组成元组，一次满足“次数降序、同次数按字母序”。

### 面向对象练习（`project_class/`）

`User` → `Admin` 继承，`Admin` 内部持有 `Privileges` 实例（组合），拆成三个模块，练习 `super()` 和“属性本身是对象”的写法。

### 模块导入练习（`project_test/`）

`make_sandwich(*foods)` 接受任意数量实参，演示 `import 模块`、`from 模块 import 函数`、`as` 别名几种导入方式及各自的调用写法。

## 测试

`ch11` 用 `pytest` 给函数和类写测试：

- 11.1 `city_functions.py` + `test_cities.py`：城市、国家格式化
- 11.2 给函数加可选形参 `population`
- 11.3 `employee.py` + `test_employee.py`：`give_raise()` 默认加薪与自定义加薪，用 `@pytest.fixture` 共享 `Employee` 实例

```sh
cd ch11
python3 -m pytest -v
```

## 算法练习

| 题目 | 方法 |
|---|---|
| 1. 两数之和 | 哈希表，边遍历边查补数 |
| 125. 验证回文串 | 双指针，跳过非字母数字 |
| 350. 两个数组的交集 II | 字典计数，`.get(c, 0) + 1` |
| 387. 字符串中的第一个唯一字符 | 哈希计数后二次遍历 |

## 每周验收

`check/` 保存前四周的验收脚本与笔记：

- `week_1.py`：列表基础，数字元素与字符串元素的区别
- `week_2.py`：字典遍历与成绩统计
- `week3.md`：函数、参数传递、返回元组、`*args`、模块导入
- `week_4.py`：文件读取 → 词频统计，是 `ch10/word_report.py` 的前身

## 目录

```
python-learning/
├── ch01–ch09/          教材逐章练习
├── ch10/               文件与异常（含 word_report.py）
├── ch11/               测试代码（pytest）
├── LeetCode/           算法题，按题号命名
├── check/              每周验收
├── notebooks/          Jupyter 环境验证
├── practice/           小实验（可变对象与副本）
├── project_class/      类、继承、组合
├── project_score_book/ 成绩记录程序
└── project_test/       模块导入练习
```

## 环境

- Python 3.12.13（虚拟环境在仓库根目录 `.venv`）
- `pytest`
- macOS（Apple Silicon）/ VS Code
- 教材：《Python 编程：从入门到实践（第 3 版）》

## 下一步

教材第一部分已完成，接下来进入项目部分（第 12 章起）；算法题继续按题号补，保持“先想测试用例、再改代码”的习惯。