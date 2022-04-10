# 随机数量 处理 验证马太效应
import random
#random.sample()生成100个不相同的随机数
alist = random.sample(range(1,101),100)

#复印一份原始数组
initcopy=alist.copy()
inilist=[]
endlist=[]
# 计算 前10名的资金合计 存入到 old 变量
old =0
sortedList = sorted( alist, reverse=True) # 得到一个排序的列表
for i in range(10):
    old=old + sortedList[i]
print ("原来资金前十名的资金合计 =",old)



#游戏规划 ，随机选两个 数 甲 和 乙 ,将 甲的一 元给乙。
#如果 甲 为零，失去游戏资格
# 运行10000次
for item in range(1,1000000):
    jia =random.randint(0,99)
    yi=random.randint(0,99)
    if (alist[jia] <=0  or alist[yi] <=0):
        continue; #没有钱没有游戏资格
    alist[jia]=alist[jia]-1 # 甲减少一元
    alist[yi] = alist[yi] + 1 # 乙增加一元

#运算结束
new =0
sortedList2 = sorted(alist, reverse=True) # 得到一个排序的列表
for i in range(10):
    new=new + sortedList2[i]
print ("运算后有资金的前十名 =",new)
