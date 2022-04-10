# 随机数量 处理 验证马太效应
import random
#random.sample()生成100个不相同的随机数
alist = random.sample(range(1,101),100)

#复印一份原始数组
initcopy=alist.copy()
inilist=[]
endlist=[]
#//输出大于90的 数的位置
for i in range(1,100):
    if (alist[i]> 90):
        print (i, "=" ,alist[i])
        inilist.append(i)

print(alist)

#游戏规划 ，随机选两个 数 甲 和 乙 ,将 甲的一 元给乙。
#如果 甲 为零，失去游戏资格
# 运行10000次
for item in range(1,100000):
    jia =random.randint(0,99)
    yi=random.randint(0,99)
    if (alist[jia] <=0  or alist[yi] <=0):
        continue; #没有钱没有游戏资格
    alist[jia]=alist[jia]-1 # 甲减少一元
    alist[yi] = alist[yi] + 1 # 乙增加一元

for i in range(1,100):
    if (alist[i]> 90): #如果大于 90元

        print (i, "=" ,alist[i])
        endlist.append(i)
print(alist)
result =list(set(inilist).intersection(set(endlist)))
print ("原来分配高90元，与后来高于90元的人的重合编号为 ",  result)
