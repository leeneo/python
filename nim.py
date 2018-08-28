##以python岗位为例，运用selenium+Chrome()爬取岗位信息
# coding=UTF-8
from lxml import etree
from selenium import webdriver
import time
import csv

browser = webdriver.Chrome()
browser.get('https://www.lagou.com/jobs/list_PYTHON?px=default&city=%E5%85%A8%E5%9B%BD#filterBox')
browser.implicitly_wait(10)

def get_dates(selector):
        items = selector.xpath('//*[@id="s_position_list"]/ul/li')
        for item in items:
            yield {
                'Name': item.xpath('div[1]/div[1]/div[1]/a/h3/text()')[0],
                'Company': item.xpath('div[1]/div[2]/div[1]/a/text()')[0],
                'Salary': item.xpath('div[1]/div[1]/div[2]/div/span/text()')[0],
                'Education': item.xpath('div[1]/div[1]/div[2]/div//text()')[3].strip(),
                'Size': item.xpath('div[1]/div[2]/div[2]/text()')[0].strip(),
                'Welfare': item.xpath('div[2]/div[2]/text()')[0]
            }
def main():
    i = 0
    for i in range(30):
        selector = etree.HTML(browser.page_source)
        browser.find_element_by_xpath('//*[@id="order"]/li/div[4]/div[2]').click()
        time.sleep(5)
        print('第{}页抓取完毕'.format(i+1))
        for item in get_dates(selector):
            print(item)
        with open('Py.csv', 'a', newline='') as csvfile:  ##Py.csv是文件的保存路径，这里默认保存在工作目录
            fieldnames = ['Name', 'Company', 'Salary', 'Education', 'Size', 'Welfare']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for item in get_dates(selector):
                writer.writerow(item)
        time.sleep(5)
    browser.close()
if __name__=='__main__':
    main()

##去除Name和Company两列
# DATA<-data[,-c(1,2)]
# ##将python字典循环写入csv文件时，标题也会被写入，去除多余的标题
# ##查找哪些行是标题重复的行
# which(DATA$Salary %in% "Salary")
#  [1]  16  32  48  64  80  96 102 118 134 150 166 182 198 214 230 246 262 278 294 310 326 342 358 374 390 406 422 438 454 470 486 502 518
# [34] 534 550 566
# ##去除多余的标题所在的行
# DATA<-DATA[-(which(DATA$Salary %in% "Salary")),]
# dim(DATA)
# [1] 545   4

##如果薪资是一个范围值，都是"-"连接，注意，薪资是一个范围值，匹配末尾结束k值需要注意，有大写K和小写k两种形式。
# newdata<-DATA[grep('\\-',DATA$Salary),]
# dim(newdata)
# [1] 544   4
# ##对比前面dim(DATA)，说明薪水少了一行，Salary具有其他的表示形式。
# ##这里将范围薪水的值分成底薪和高薪两部分，后面取平均值来表示薪水
# library(tidyr)
# library(stringr)
# newdata<-separate(data=newdata,col=Salary,into=c("lowsalary","highsalary"),sep="-")
# ##分别去除后面的k值，注意k有大写和小写两种形式
# newdata$lowsalary<-str_replace(newdata$lowsalary,'k|K',"")##  |表示或的关系
# newdata$highsalary<-str_replace(newdata$highsalary,'k|K',"")
# newdata$lowsalary<-as.numeric(newdata$lowsalary)##转换数据类型
# newdata$highsalary<-as.numeric(newdata$highsalary)
# newdata$salary<-(newdata$lowsalary+newdata$highsalary)/2
# newdadat<-newdata[,-c(1,2)]##去除原有的lowsalary和highsalary

###Education部分
##首先将Education中工作经验和学历分开
# newdata<-separate(data = newdata,col=Education,into=c("Experience","Graduate"),sep = '/')
# table(newdata$Experience)
# 经验1-3年     经验1年以下       经验3-5年      经验5-10年        经验不限  经验应届毕业生  
#  187               6             261              46              37               7 
# table(newdata$Graduate)
#  本科  不限  大专  硕士 
#   447    27    63     7 

# ##此处以公司人数作为描述公司规模的标准
# newdata<-separate(data=newdata,col=Size,into=c('Type','Rong','Number'),sep='/')
# table(newdata$Number)

#  15-50人   150-500人  2000人以上    50-150人  500-2000人    少于15人 
#    76         139         117         119          82          11 
# table(newdata$Rong)
# A轮          B轮          C轮    D轮及以上   不需要融资     上市公司       天使轮       未融资  
# 86           81           54           30          132           80           33           48 
# ##将Type去除   
# newdata<-newdata[,-3]

# Welfare<-newdata[,"Welfare"]
# ##将Welfare去除
# newdata<-newdata[,-5]
# head(newdata)

# 数据分析部分

# 1.工资与工作年限的关系
# library(ggplot2)
# ggplot(newdata,aes(x=Experience,y=salary))+geom_boxplot(col="red")

# 2.工资与学历的关系（专科，本科，研究生，不限）
# ggplot(newdata,aes(x=Graduate,y=salary))+geom_boxplot(col="red")

# 3.工资与公司融资的关系
# ggplot(newdata,aes(x=Rong,y=salary))+geom_boxplot(col="red")

# 4.工资与公司大小的关系
# 公司规模越大，平均的工资也越高。

# 5.工资与工作时间和学历的关系
# library(ggthemes)
# library(scales)
# ggplot(newdata,aes(x=Experience,y=salary,fill=factor(Graduate)))+
# geom_boxplot()+
# geom_hline(aes(yintercept=20),color="red",linetype="dashed",lwd=1)+
# scale_y_continuous(labels=dollar_format())+theme_few()

# 6.公司福利的云图
# ##公司福利的云图
# library(jiebaR)
# Welfare<-as.character(Welfare)
# wk = worker()
# seg_words<-wk[Welfare]
# library(plyr)
# library(wordcloud)
# tableWord<-count(seg_words)
# windowsFonts(myFont=windowsFont("华文彩云")) ##使用华文彩云字体
# wordcloud(tableWord[,1],tableWord[,2],random.order=F,col= rainbow(100),family="myFont")