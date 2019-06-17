#coding=utf-8
'''
Created on 2019年6月17日

@author: ale
'''
import requests
import re
import math
import os
import shutil
#获取女神合集编号list
def getUrls(url,path):
    req=requests.get(url)
    html=req.text
    reg = '/g/.+?\/' 
    ref=re.compile(reg)
    fans=ref.findall(html)
    list=[]
    #过滤页面
    for element in fans :
        if(element not in list):
            list.append(element)
    getMainpage(list,path) 
#获得主页面地址list                
def getMainpage(list,path):
    url='https://www.nvshens.com/'
    urls=[]
    for temp in list:
        rurl=url+temp
        getPage(rurl,path)
#获取文件头加页码        
def getPage(url,path):
    req=requests.get(url)
    html=req.text
    #获取照片总数re
    reg = r'<span style=\'color: #DB0909\'>(.*?\张照片)</span>' 
    #获取文件名re
    reg1 = r'<h1 id="htilte">(.*?)</h1>'
    ref=re.compile(reg)
    ret=re.compile(reg1)
    title=ret.findall(html)
    title=title[0]
    num=ref.findall(html)
    if len(num)==1:
        nums=list(filter(str.isdigit, num[0]))
        nums="".join(nums)
    pages=math.ceil(int(nums)/3)
    for i in range(1,pages+1):
        minurl=""
        if(i!=1):
            minurl=url+str(i)+'.html'
        else:
            minurl=url    
        print(minurl+"  "+title)
        downloadPic(minurl,title,path)
#主程序        
def downloadPic(url,title,path):
    req=requests.get(url)
    html=req.text
    path=path+'\\'+title
    if not os.path.exists(path):
        os.makedirs(path)
        print("创建"+path)    
    #
    reg=r'img src=\'(.+?\.jpg)'
    rep=re.compile(reg)
    pics=rep.findall(html)
    for pic in pics:
       name=pic.split('/')[-1]
       picc=requests.get(pic)
       with open(path+'\\'+name, 'wb') as f:
                f.write(picc.content)
                print (path+'/'+name+ '下载完成')                       
if __name__ == '__main__':
    path=r'E:\nvshen\qibao'
    if not os.path.exists(path):
        os.makedirs(path)
        print("创建"+path)
    else:
        print("文件夹已存在"+path) 
    url='https://www.nvshens.com/girl/17596/album/'
    getUrls(url,path)
