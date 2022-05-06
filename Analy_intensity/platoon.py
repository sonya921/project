import itertools
import csv
import pandas as pd

def testIntensityCAV(p,N11,N,n): #已知渗透率，跟驰，车队总数进行强度计算
    O11=[]
    for i in range (len(N11)):
        O=N11[i]/(N-1)
        O11.append(O)
    return O11


def FollowCAV(UPList): #cav-cav跟驰数量计算
    Num_N11=[]
    for i in range(len(UPList)):
        UPList1=UPList[i]
        N11=0
        for j in range(len(UPList1)-1):

            if UPList1[j]==UPList1[j+1]==1:
                N11+=1
        Num_N11.append(N11)
    return Num_N11



def Permutation(str, beg, endl):#全排列去重
    if beg == endl - 1:
        UPList.append(str[:])
        #print(a)
        #UPList.append(str)
        return
    for i in range(beg, endl):
        if str[i] in str[beg:i]:
            continue
        str[i], str[beg] = str[beg], str[i] #
        Permutation(str, beg+1, endl)       #递归
        str[beg], str[i] = str[i], str[beg] #前后倒置去重
for N in [13,15,18,20,22,24,26]:
    for p in [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]:#主要执行部分
        UPList = []                                #每组车队根据全排列做出的去重
        # N = 25                             #车队数量数值
        n=int(p*N)                                 #种类车辆数计算
        l=N-n                                      #种类车辆数计算
        VehList=[0]*l+[1]*n                        #生成车队数组
        beg = 0
        endl = len(VehList)
        list1=Permutation(VehList, beg, endl)      #函数调用
        #print(UPList)
        N11=FollowCAV(UPList)                      #CAV-CAV跟驰数量计算

        dict = {}
        for i in range(N+1):                       #每个渗透率下跟驰数量文件输出

            dict[i]=N11.count(i)
        nam = str(N)+ '.csv'
        # nam='200.csv'
        f = open(nam, mode='a', encoding='utf-8', newline='')
        csv_writer = csv.DictWriter(f, fieldnames=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                                                   20,21,22,23,24,25,26])
        csv_writer.writeheader()
        csv_writer.writerow(dict)
        # N12 =[]
        # N12=N11.count(i)
    # print(dict)
    # nam=str(p)+'.csv'
    # doc=open(nam,'w',encoding='utf-8')
    #     # print(Fin_O11)
    # print(dict,file=doc)
    # doc.close()









