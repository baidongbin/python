import pygal

x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
# 定义 2 个列表分别作为两组柱状图的 Y 轴数据
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]
# 创建 pygal.Bar 对象（柱状图）
bar = pygal.Bar()
# 添加两组代表条柱的数据
bar.add('疯狂 Java 讲义', y_data)
bar.add('疯狂 Android 讲义', y_data2)
# 设置 X 轴的刻度值
bar.x_labels = x_data
bar.title = '疯狂图书的历年销量'
# 设置 X、Y 轴的标题
bar.x_title = '年份'
bar.y_title = '销量'
# 设置 X 轴的刻度值旋转 45 度
bar.x_label_rotation = 45
# 设置将图例放在底部
bar.legend_at_bottom = True
# 设置数据图四周的页边距
# 也可通过 margin_bottom、margin_left、margin_right、margin_top 只设置单独一边的页边距
bar.margin = 35
# 隐藏 X 轴上的网格线
bar.show_y_guides = False
# 显示 X 轴上的网格线
bar.show_x_guides = True
# 指定将数据图输出到 SVG 文件中
bar.render_to_file('fk_books.svg')
