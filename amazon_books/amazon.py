
from selenium import webdriver
import csv

driver = webdriver.Chrome(r"E:\iti_ai_pro\data_preparation_and_expolration\New folder\chromedriver.exe")

driver.get('https://www.amazon.in/gp/bestsellers/books/')

books = driver.find_elements_by_xpath("//div[@class='p13n-sc-truncated']")
prices = driver.find_elements_by_xpath("//span[@class='p13n-sc-price']")


for i in books:
    print(i.text)
    
    

for i in prices:
    print(i.text)




with open(r'E:\\iti_ai_pro\\data_preparation_and_expolration\\task2_webScrap\amazon_books.csv', 'w',encoding='utf-8',newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Book','Price'])
    for i in range(0,len(books)):
        csvwriter.writerow([books[i].text,prices[i].text])