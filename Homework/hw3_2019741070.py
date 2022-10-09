from selenium import webdriver
import wordcloud
import matplotlib.pyplot as plt

#크롬 드라이버
driver = webdriver.Chrome('C:/Users/rs555//Desktop/AIProgramming/chromedriver_win32/chromedriver')
driver.implicitly_wait(1)
#url
driver.get(url="https://namu.wiki/w/KBO%20%EB%A6%AC%EA%B7%B8") 

driver.implicitly_wait(time_to_wait=5)
#find_element_by_xpath(find_element('xpath')이용하여 문서 크롤링)
element_xpath=driver.find_element('xpath','//*[@id="jWZtJ8Cjb"]')
#text만 element에 저장
element=element_xpath.text

print(element)
#stopwords 설정
s_words=wordcloud.STOPWORDS.union({'있다','수 있는', '경우가','이는','그러나', '없는', '편이다', '큰', '것','및','있지만','것은','그','것이다','한','등','다른','이후','모든'})
#워드 클라우드
image = wordcloud.WordCloud(font_path='C:/Users/rs555/Desktop/AIProgramming/malgun-gothic/malgun.ttf',width=1000, height=700,stopwords=s_words).generate(element)

plt.figure(figsize=(40,30))
plt.imshow(image)
plt.show()

driver.close()

