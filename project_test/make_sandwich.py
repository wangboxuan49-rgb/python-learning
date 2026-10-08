#  功能:模块应用
#  作者:wbx
#  日期:2026-09-25

import sandwich #导入整个模块,调用函数时需要指定导入模块名称
#from sandwich import make_sandwich     导入模块中指定的任意数量函数，调用时无需指定模块名称
#from sandwich import make_sandwich as ms   给函数指定别名，调用时只用使用别名
#import sandwich as s   导入整个模块并指定别名，调用时指定模块别名
#from sandwich import *    导入模块中所有函数，调用时无需指定模块名称（有重复名称的风险）

sandwich.make_sandwich('beef')
sandwich.make_sandwich('fish','beef','pork')
sandwich.make_sandwich('beef','chicken')