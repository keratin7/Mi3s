from selenium.webdriver import Chrome
driver = Chrome()
driver.get("http://www.mi.com/in/events/diwali2016/")
driver.findElement(By.xpath("//*[@id='redmi']/div/div/ul/li[1]/div[2]/a")).click()