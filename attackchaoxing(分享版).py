import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

attackurl = "https://passport2.chaoxing.com/login?fid=&newversion=true&refer=https%3A%2F%2Fi.chaoxing.com"

# 设置Chrome浏览器的驱动路径
#driver_path = "C:\\Users\\14845\\Desktop\\AI TECHNOLOGY\\chromedriver-win64\\chromedriver.exe"
#user_data_dir = "C:\\Users\\14845\\AppData\\Local\\Google\\Chrome\\User Data\\"

# 创建一个Chrome浏览器实例,使用chrome的用户账户，并抹除使用driver操作的痕迹
options = webdriver.ChromeOptions()
options.add_argument(f'--disable-blink-features=AutomationControlled')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0')
#options.add_argument(f'user-data-dir={user_data_dir}')
options.headless = False  # 取消headless模式以便调试

driver = webdriver.Chrome(options=options)

driver.get(attackurl)

# 等待5秒以确保页面加载
time.sleep(5)

# 输入手机号和密码并登录
phonenumber = input("请输入你的账户电话号码: ")
password = input("请输入超星登录密码: ")
#注意代码完成后要及时删除个人账户密码改用手动输入！！！！！

driver.find_element(By.XPATH, '//*[@id="phone"]').send_keys(phonenumber)
driver.find_element(By.XPATH, '//*[@id="pwd"]').send_keys(password)
driver.find_element(By.XPATH, '//*[@id="loginBtn"]').click()

# 等待页面加载完成
time.sleep(5)

# 获取登录后的cookies
cookies = driver.get_cookies()
session_cookies = {cookie['name']: cookie['value'] for cookie in cookies}

    
# 设置请求头
headers = {
    'Accept': 'text/html, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '80',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'mooc1-1.chaoxing.com',
    'Origin': 'https://mooc1-1.chaoxing.com',
    'Referer': 'https://mooc1-1.chaoxing.com/visit/interaction?s=aac500ead1a6ac27f1273b9fa41164b1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

# 设置请求数据
data = {
    'courseType': '1',
    'courseFolderId': '0',
    'baseEducation': '0',
    'superstarClass': '',
    'courseFolderSize': '0'
}

# 发送请求获取课程列表
response = requests.post('https://mooc1-1.chaoxing.com/mooc-ans/visit/courselistdata', headers=headers, cookies=session_cookies, data=data)

#等待回复
time.sleep(1)

if response.status_code == 200:
    print("成功获取课程列表")
    #print(response.text)
else:
    print("获取课程列表失败")
    print(response.status_code)

#使用BS解析resp
soup = BeautifulSoup(response.content, "html.parser")
fucking_fake_resp = soup.find_all("a")
#print(fuck)
#for a in fucking_fake_resp:
    #muther_fucker_fake_website = a.get('href')
    #print(muther_fucker_fake_website)
    #in order to solve the fucking error the bitch chaoxing sent to us , i have no chance but to delete the ass of chaoxing ,which is "amp;"
    # 使用正则表达式替换`&amp;`为`&`
    #muther_fucker_website = re.sub(r'&amp;', '&', muther_fucker_fake_website)
    #print(muther_fucker_website)
    # 在不关闭前一个chrome窗口的情况下，使用chromedriver在原窗口的新选项卡中打开你妈的课程链接
    #driver.execute_script(f'window.open("{muther_fucker_website}")')
    
    # 切换到新选项卡
    #driver.switch_to.window(driver.window_handles[-1])
    #这段代码可以用来恶心慰问他妈的超星服务器，BYD
# 定义目标课程名称
target_course_name = input("请输入你想要使用的超星课程全称，即在页面上的课程全名：")
#做完了换回手动输入！！！！

# 查找包含目标课程名称的a标签
target_link = None
for a_tag in soup.find_all('a', class_='color1'):
    span_tag = a_tag.find('span', class_='course-name overHidden2')
    if span_tag and span_tag.get('title') == target_course_name:
        target_link = a_tag['href']
        break
print(target_link)

# 修正链接中的&amp;
if target_link:
    target_link2 = re.sub(r'&amp;', '&', target_link)
    print("找到目标课程", target_course_name, "链接：", target_link2)
else:
    print("未找到目标课程链接")
fuck = target_link2
# 在不关闭前一个chrome窗口的情况下，使用chromedriver在原窗口的新选项卡中打开你妈的课程链接
driver.execute_script(f'window.open("{fuck}")')
    
# 切换到新选项卡
driver.switch_to.window(driver.window_handles[-1])

time.sleep(5)

#找到你老师在超星布置的任务，此处以视频学习为例
tag = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[1]/div/ul[1]/li[2]')
#此处是个傻逼的动态内容，不能直接点击而是要触发一个JS代码
driver.execute_script("arguments[0].click();", tag)

#点击第一章节的链接,but not work as chaoxing is son of bitch that hide this link into iframe.
#tag2 = driver.find_element(By.XPATH('/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/ul/li[1]')
#driver.execute_script("arguments[0].click();", tag2)

#因为超星把他妈的你的课程视频藏在鸡巴的iframe里面，所以还要干进去他麻痹的iframe里面

#first,find the xpath of the fucking iframe
iframe_xpath1 = '/html/body/iframe'

#second, move to that mutherfucker iframe
iframe1 = driver.find_element(By.XPATH,iframe_xpath1)

#last, switch to that bitch iframe
driver.switch_to.frame(iframe1)

#你妈死了，勾巴傻卵chaoxing，但是不得不说，负责网页开发的的确辛苦了，注释做的很全。
#下一步找到并点击视频链接
# 使用 XPath 查找所有 title 为 “视频学习” 的 div 元素
divs_with_video_study = driver.find_elements(By.XPATH, "//div[@title='视频学习']")
#因为超星可能在页面刷新时动了手脚，导致循环时上一次找到的元素下一次不可用，现在尝试先拿出视频网页的数量再循环几次
muther_fucker_count = len(divs_with_video_study)
print(muther_fucker_count)
#abandon = {1,2,3,4,5,6,7,8,9}

for a in range(muther_fucker_count):
    b = a + 1
    # 切换到新选项卡
    #driver.switch_to.window(driver.window_handles[-1])
    try:
        divs_with_video_study2 = driver.find_elements(By.XPATH, "//div[@title='视频学习']")
        #element.click()
        divs_with_video_study2[a].click()
        print(f"点击了第{b}个视频")
    except Exception as e:
        print(f"点击第{b}个视频出错: {e}")
    #//*[@id="cur856822833"]


    #tag3 = driver.find_element(By.XPATH,'//*[@id="cur856822828"]/div/div[2]/a')
    #tag3.click()
    #等待加载完成
    time.sleep(5)

    print("如果可以看到这句话，应该是已经成功进入了超星学习界面")
    #退出iframe,然后切回这个重新刷新的学习界面
    driver.switch_to.window(driver.window_handles[-1])

    #开始播放视频
    #because the video is still under one and another fucking iframe now switch it.
    #此处使用fucker 以及 one another 表达了作者的什么感情？（150分）
    #fucker 时英语中下流词汇， one another 在英语中表示一个接着一个，此处生动形象的表达了作者对超星学习通的厌恶之情，以及暗中讽刺了超星为了防止大学生偷懒搞套娃一般的网页结构恶心人的操作。
    #first,find the xpath of the fucking iframe（梅开二度）
    iframe_xpath2 = '/html/body/div[6]/div/div[3]/div[7]/iframe'
    #/html/body/div[6]/div/div[3]/div[7]/iframe
    #second, move to that mutherfucker iframe（梅开二度）
    iframe2 = driver.find_element(By.XPATH,iframe_xpath2)

    #last, switch to that bitch iframe（梅开二度）
    driver.switch_to.frame(iframe2)

    #first,find the xpath of the fucking iframe（三羊开泰）
    iframe_xpath3 = '/html/body/div[2]/div/p[1]/div/iframe'

    #second, move to that mutherfucker iframe（三羊开泰）
    iframe3 = driver.find_element(By.XPATH,iframe_xpath3)

    #last, switch to that bitch iframe（三羊开泰）
    driver.switch_to.frame(iframe3)

    #在这个视频的iframe中，终于！我找到了视频的播放按钮！（藏得真几把深）
    fuckingplaybutton = '/html/body/div[2]/div[3]/div[2]/div/button'
    print('如果到这里还没有报错，那么恭喜你，成功的进入了超星的视频播放界面')#这个藏着一堆反爬虫与干反向识别用户行为的代码（某种意义上已经侵犯了客户隐私的）的页面
    #尝试点击播放
    driver.find_element(By.XPATH,fuckingplaybutton).click()
    print("已点击，请查看视频是否真的播放了")
    time.sleep(15)

    #等待视频结束
    #定位并找到关于视频时长描述的标签
    #video_time = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[2]/div/div[6]/div[4]/span[2]')
    #print(video_time)
    # 获取网页内容
    html1 = driver.page_source

    # 使用BeautifulSoup解析网页内容
    soup = BeautifulSoup(html1, 'html.parser')

    #找到时长
    videotime = soup.find_all('span',{"class":"vjs-duration-display"})
    print(videotime)
    for span in videotime:

        span1 = span.text
        print (span1)
        time_str = span1
        #定义了一个时间的换算方式
        def time_to_seconds(time_str):
            # 分割时间字符串，假设格式是 "mm:ss"
            minutes, seconds = map(int, time_str.split(':'))
            # 计算总秒数
            total_seconds = minutes * 60 + seconds
            return total_seconds
        #...
        total_seconds = time_to_seconds(time_str)
        print("总秒数:", total_seconds)

    #等待视频结束 
    time.sleep(total_seconds)
    print('视频此时应该结束，若没有请等待视频结束后再操作')
    time.sleep(10)
    #a = input('视频结束了吗？（Y/N）：')
    #if a:
        #a = 'Y'
    #else:
        #print('时间差不多喽，10s倒计时！')
        #time.sleep(10)
    print("跳转到下一个视频")
        
    #返回原来的界面，重新进入iframe, 接着看下一条视频
    #退出iframe
    driver.refresh()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[-1])
    #点击返回按钮
    backbutton = driver.find_element(By.XPATH,'/html/body/div[6]/div/div[1]/a')
    backbutton.click()
    #等待加载完成
    time.sleep(10)

    driver.switch_to.window(driver.window_handles[-1])

    #重新进入课程界面的iframe
    #first,find the xpath of the fucking iframe
    iframe_xpath11 = '/html/body/iframe'

    #second, move to that mutherfucker iframe
    iframe11 = driver.find_element(By.XPATH,iframe_xpath11)

    #last, switch to that bitch iframe
    driver.switch_to.frame(iframe11)
    #此处之后，回到循环的开始再看下一条视频

print("看到这里说明已经自动刷完了所有视频，请在浏览器退出后再次手动登录超星，查看课程是否真的完成了。")
# 关闭浏览器
driver.quit()
print("end")

#https://mooc1-1.chaoxing.com/mooc-ans/visit/stucoursemiddle?courseid=206889434&amp;clazzid=79057736&amp;vc=1&amp;cpi=228506923&amp;ismooc2=1&amp;v=2
#https://mooc1-1.chaoxing.com/mooc-ans/visit/stucoursemiddle?courseid=243068125&clazzid=98990733&vc=1&cpi=228506923&ismooc2=1&v=2
#https://mooc2-ans.chaoxing.com/mooc2-ans/mycourse/stu?courseid=243068125&clazzid=98990733&cpi=228506923&enc=d6289cf71986bf7801db635080683570&t=1719222983745&pageHeader=0&v=2
