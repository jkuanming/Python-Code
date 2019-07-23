file1 = open('test\scores ranking\scores.txt','r',encoding='gbk') 
file_lines = file1.readlines() 
file1.close()

final_scores = []

for i in file_lines:
    data =i.split()
    sum = 0  # 先把总成绩设为0
    for score in data[1:]:  # 遍历列表中第1个数据和之后的数据
        sum = sum + int(score)  # 然后依次加起来，但分数是字符串，所以要转换    
    result = data[0]+str(sum)+'\n'  # 结果就是学生姓名和总分
    print(result)
    final_scores.append(result)

print(final_scores)

sum1 = open('test\scores ranking\winner_eg1.txt','w',encoding='utf-8') 
sum1.writelines(final_scores)
sum1.close()

file2 = open('test\scores ranking\winner_eg1.txt','r',encoding='utf-8') 
file_lines = file2.readlines() 
file1.close()

dict_scores = {}
list_scores = []
final_scores = []

# print(file_lines) 
# print(len('\n')) 

# 打印结果为：['罗恩102\n', '哈利383\n', '赫敏570\n', '马尔福275\n']
# 经过测试，发现'\n'的长度是1。所以，名字是“第0位-倒数第5位”，分数是“倒数第4位-倒数第二位”。
# 再根据“左取右不取”，可知：name-[:-4],score-[-4:-1]

for i in file_lines:  # i是字符串。
    print(i)
    name = i[:-4]  # 取出名字（注：字符串和列表一样，是通过偏移量来获取内部数据。）
    score = int(i[-4:-1])  # 取出成绩
    print(name)
    print(score)
    dict_scores[score] = name  # 将名字和成绩对应存为字典的键值对(注意：这里的成绩是键)
    list_scores.append(score)

# print(list_scores)
list_scores.sort(reverse=True)  # reverse，逆行，所以这时列表降序排列，分数从高到低。
# print(list_scores)

for i in list_scores:
    result = dict_scores[i] + str(i) + '\n'
    # print(result)
    final_scores.append(result)

print(final_scores)  # 最终结果

winner_new = open('test\scores ranking\winner_new.txt','w',encoding='utf-8') 
winner_new.writelines(final_scores)
winner_new.close()
