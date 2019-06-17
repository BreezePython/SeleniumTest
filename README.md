> From： 来自我的微信公众号：[清风Python]

### 写在前面的话
昨天说到，之后一阵子，打算把selenium的知识进行一个复习和系统的总结。要说明以下几点：
1. 因为是系统的总结，所以文章具备连贯性，但我尽量将较为集中的知识点整理在一起发
2. 由浅入深的知识内容，开篇肯定不会有太多的技术涉及，觉得无趣还望轻喷
3. 并不是所有朋友都喜欢或都有意愿学习selenium，所以在这个系列中还是会穿插发一些其他的文章
4. 毕竟文章的总结是基于python和selenium知识的，其中会涉及测试设计等方面，但不是文章重点，故不会过于详细的说明
5. 这个系列会在公众哈偶的底部的文章分类单独开一个窗口进行集中收录，只是希望自己能坚持把这个系列的文章写完
6. 欢迎催更与错误问题指正，但公众号一经发布的文章，无法修改，故对应的简书[清风python](https://www.jianshu.com/u/d23fd5012bed)会同步更新

### 学习selenium能做什么？
很多书籍、文章中是这么定义selenium的：
> Selenium 是开源的自动化测试工具，它主要是用于Web 应用程序的自动化测试，不只局限于此，同时支持所有基于web 的管理任务自动化。

可如果要是这么介绍selenium，估计明天关注我的人80%都要弃坑了，我又不是测试、我学什么selenium。wait a moment！先别取关...
请仔细读读后半句，**支持所有基于web的管理任务和自动化**！
什么算基于web的任务,就只是自动化测试？非也非也，只要是通过浏览器访问的事件，都可以算在内啊！
如今，越来越多的反爬虫技术（千奇百怪的登陆验证、接口调用中的cookie验证、异步动态加载、等等...），是你没办法直接通过requests完成获取相关数据。这时候，你就可以使用selenium，模拟浏览器操作，自动化完成你的数据获取。

### 简单介绍selenium
公众号里面写上selenium的前世今生，你们肯定直接觉得篇幅太长懒得看了,那我简单的概括下：
1. Jason Huggins 在2004年任职于ThoughtWorks时，发起了Selenium项目
2. selenium存在三个版本1.0、2.0、3.0，**且即将推出4.0**
3. Selenium 1.0 = Selenium IDE + Selenium Grid + Selenium RC
	- Selenium IDE是嵌入到Firefox浏览器中的一个插件，实现简单的浏览器操作的录制与回放功能
	- Selenium Grid是一种自动化的测试辅助工具，Grid通过利用现有的计算机基础设施，能加快Web-App的功能测试
	- Selenium RC分为Client Libraries和Selenium Server。Client Libraries库主要用于编写测试脚本，用来控制Selenium Server的库
5. Selenium 2.0 推出了WebDriver用来替代Selenium RC（主推： WebDriver 备胎:Selenium RC）
6. Selenium 3.0 WebDriver彻底替代了Selenium Grid
7. WebDriver封装了基础的协议规范，WebDriver **针对各个浏览器而开发**(所以针对不同浏览器，需要下载不同的webdriver)，用来控制浏览器
8. 支持主流的编程语言，包括：Java、Python、C#、PHP、Ruby、JavaScript等

针对我们Python学习的内容，就是:
> 如何通过WebDriver封装的基础协议，完成正确的代码编写，从而控制浏览器进行成语接龙，为所欲为--为所欲为--为...

### 学习准备
- Python3.5+，我使用的3.6.8...
- 顺手的编辑器，我选择的pycharm
- 配置好包管理工具pip，使用`pip install selenium`，完成selenium(selenium-3.141.0)的安装
- selenium支持多种浏览器，但差别仅仅是需要下载不同的Webdriver，所以挑一款浏览器即可，
我选择Chrome(v70版本)，不知道版本怎么看？(浏览器输入：chrome://settings/help)
- 下载对应浏览器及版本对应的Webdriver，并配置环境变量
- 不半途而废的信心，over...

Chrome浏览器版本对应的Webdriver版本信息如下：

|ChromeDriver版本|支持的Chrome版本|
|:--:|:--:|
|v2.46|v72-74|
|v2.45|v71-73|
|v2.44|v70-72|
|v2.43|v69-71|
|v2.42|v68-70|
|v2.41|v67-69|
|v2.40|v66-68|
|v2.39|v66-68|
|v2.38|v65-67|
|v2.37|v64-66|
|v2.36|v63-65|
|v2.35|v62-64|
|v2.34|v61-63|
|v2.33|v60-62|
|v2.32|v59-61|
|v2.31|v58-60|
|v2.30|v58-60|
|v2.29|v56-58|
|v2.28|v55-57|
|v2.27|v54-56|
|v2.26|v53-55|
|v2.25|v53-55|
|v2.24|v52-54|
|v2.23|v51-53|
|v2.22|v49-52|
|v2.21|v46-50|
|v2.20|v43-48|
|v2.19|v43-47|
|v2.18|v43-46|
|v2.17|v42-43|
|v2.13|v42-45|
|v2.15|v40-43|
|v2.14|v39-42|
|v2.13|v38-41|
|v2.12|v36-40|
|v2.11|v36-40|
|v2.10|v33-36|
|v2.9|v31-34|
|v2.8|v30-33|
|v2.7|v30-33|
|v2.6|v29-32|
|v2.5|v29-32|
|v2.4|v29-32|

ChromeDriver下载，推荐大家使用[华为开源镜像站](https://mirrors.huaweicloud.com/)，下载对应系统的Webdriver，Webdriver为一个单独的exe文件，如何配置是它生效？最懒的版本是丢到你的python安装根目录，亦或者你单独找个私密的地址存起来，然后在环境变量的path中添加配置该地址。