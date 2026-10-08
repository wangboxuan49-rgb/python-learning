#  功能:发送消息
#  作者:wbx
#  日期:2026-09-25

def show_messages(messages):        #函数功能：遍历列表，打印元素
    for message in messages:
        print(message.title())
    print()

def send_messages(u_messages, s_messages):  #函数功能：将元素从原先列表移到新列表当中
    while u_messages:
        current_message = u_messages.pop()
        s_messages.append(current_message)

unsent_messages = ['hello','thanks','sorry']
sent_messages = []

show_messages(unsent_messages)
send_messages(unsent_messages, sent_messages)   #位置实参
#如果不想修改原先列表，可以使用副本作为实参，如 unsent_messages[:]
show_messages(unsent_messages)      #检查原先列表
show_messages(sent_messages)        #检查新列表元素