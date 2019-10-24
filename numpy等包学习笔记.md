**涉及到的包：numpy、matplotlib、os**

---

1.[数组维度，形状，大小](https://blog.csdn.net/code_fighter/article/details/80371535)

2.[数组维度，sum维度](https://zhuanlan.zhihu.com/p/48871067)

3.[Python operator.itemgetter函数理解](https://blog.csdn.net/qq_22022063/article/details/79019294)

4.[matplotlib.pyplot画图，面向对象方式和面向过程方式](https://blog.csdn.net/you_are_my_dream/article/details/53439518)

5.[数组、矩阵拼接](https://blog.csdn.net/guofei_fly/article/details/85485173)

6.[os.listdir() 方法](https://www.runoob.com/python/os-listdir.html)

7.找到两个list中的共同元素可以使用集合set

---

常用方法：

```python
array.min(axis)
array.max(axis)
array.sum(axis)
array.shape  #成员变量，返回tuple
array.ndim   #成员变量，返回维度int

file.readlines()  #返回tuple
file.readline()

numpy.tile(array_like,(rows,cols))

numpy.sort(array_like,key=none,reverse=false)  # 与key = operator.itemgetter(axis)配合使用
                                               # https://www.cnblogs.com/zhoufankui/p/6274172.html
                                               # 实现按行记录的某一列属性值的大小排序
numpy.zeros(shape)  #零矩阵
numpy.eye(dim) #创建dim阶单位矩阵

os.listdir()

str.strip(str) #移除字符串开头和末尾的字符或者字符串(默认为空格和换行符)

str.split(str,num) #以str分割字符串,若给出num则分割为num+1个子串
```

---

matplotlib画图(面向对象)

```python
import matplotlib

import matplotlib.pyplot as plt

# 创建figure对象
fig = plt.figure()
# 创建子图,222表示2X2的子图中的第一个
ax1 = fig.add_subplot(221)
# 绘制散点，s=size，c=color，label图例
ax1.scatter(x,y,s,c,label)
# 绘制折线图
ax1.plot(x,y,s,c,label)
# 图例显示
plt.legend(loc='best')
#坐标轴文本
plt.xlabel('x'，fontdict={'family' : 'Times New Roman', 'size'   : 16})

plt.ylabel('y')
# 显示
plt.show()
```

---

[pandas读取文件](https://blog.csdn.net/cindy407/article/details/90747049)

csv读取简单示例:

```python
data = pd.read_csv('data.csv',encoding='gbk',header=None)  # data为DataFrame类型，不可以直接索引
data = np.array(data)
```

txt读取简单示例:

```python
data = pd.read_table('data.txt',sep=',',encoding='gbk',header=None)
data = np.array(data)
```

---

[正则表达式](https://www.runoob.com/regexp/regexp-intro.html)

[python正则表达式(注意区分match方法和search方法)](https://www.runoob.com/python/python-reg-expressions.html)

生成正则表达式:`r=re.compile('\\W+')`(返回一个pattern对象，直接写成''\W+'也是可以的)或者`r=r'\W+'`

---

[随机数random包](https://www.cnblogs.com/mfryf/p/4556007.html)

随机整数`random.randint(min.max)`

[另有numpy.random方法](https://www.cnblogs.com/sench/p/9683905.html)

[随机种子理解](https://blog.csdn.net/youhuakongzhi/article/details/90572969)

---

性能分析模块 timit

---

python原地刷新输出

```python
import time
for i in range(100):
    print('%d%%'%i,end='\r',flush=True)
    time.sleep(0.1)
#只有在终端有效，解释器中自带的输出无效
```
