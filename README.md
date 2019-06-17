# python_demo
上传python代码
if __name__ == '__main__方法中输入你要爬的妹子的网址，我这边用的是集合网址

getUrls方法解析所有的图集后缀

getMainpage方法获得所有图集的网址

getPage因为网站是按三张图片分页的，所以通过爬取网页上的张数来得到该图集的所有子路径

然后就是解析src和文件名来下载啦
