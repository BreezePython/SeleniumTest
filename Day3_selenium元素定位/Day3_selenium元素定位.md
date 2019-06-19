##### 关于昨天的文章
今天有朋友反馈，代码运行的时候，selenium提示警告
> DeprecationWarning: use options instead of chrome_options
> driver = webdriver.Chrome(chrome_options=options)

本来以为是我的selenium版本太低了，可以上官网看到3.141.0是最新版本啊，最后把python从3.6.8升级到3.7.3才复现了此问题。虽然这个告警不影响使用，但既然官方提示了修改就看看呗，其实很简单：
```python
# 将原本的chrome_options
driver = webdriver.Chrome(chrome_options=options)
# 改为options 即可
driver = webdriver.Chrome(options=options)
# 另外，针对以下引用
from selenium.webdriver.chrome.options import Options
options = Options()
# 可以简写为：
options = webdriver.ChromeOptions()
```

##### 今天说什么
今天肯定说元素定位啊，再不说都要取关了...可应该怎么说呢？
话说，selenium1.0起初它使用了基于Javascript的自动化引擎，而浏览器对 Javascript 又有很多安全限制，之后后通过webdrvier进行了各浏览器的协议封装。那么说到底，我们通过selenium变相的完成了js的的相关操作，比如：

