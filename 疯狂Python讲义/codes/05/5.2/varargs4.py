def test(name, message):
    print('用户是：', name)
    print('欢迎消息：', message)


my_list = ['孙悟空', '欢迎来疯狂软件']
test(*my_list)


def foo(name, *nums):
    print('name参数：', name)
    print('nums参数：', nums)


my_tuple = (1, 2, 3)
foo('fkit', *my_tuple)
# 使用逆向收集，将my_tuple元组的第一个元素传给name参数，剩下的元素传递给nums参数
foo(*my_tuple)
# 不使用逆向收集，my_tuple元组整体传给name参数
foo(my_tuple)


def bar(book, price, desc):
    print(book, ' 这本书的价格是：', price)
    print('描述信息', desc)


my_dict = {'price': 89, 'book': '疯狂Python讲义', 'desc': '这是一本系统全面的Python学习图书'}
# 按你想手机的方式将my_dict的多个key-value对传给bar()函数
bar(**my_dict)
