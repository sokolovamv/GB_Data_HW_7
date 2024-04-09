# Импорт необходимых библиотек
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import time

# Установка веб-драйвера
driver = webdriver.Chrome()

# Переход на веб-сайт DuckDuckGo
driver.get("https://www.litres.ru")

# Поиск строки поиска и ввод поискового запроса Драма
search_bar = driver.find_element(By.NAME, "q")
search_bar.send_keys("дюна")

# Поиск кнопки поиска и нажатие на нее
search_button = driver.find_element(By.XPATH, "//button[@type='submit']")
search_button.click()

wait = WebDriverWait(driver, 10)


result_data = []


# Переход на первую страницу веб-сайта
result_data = []

results = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='ArtV2Default_cover__text__k3N4V']")))


# Извлечение информации каждой книги
for result in results:
    result_title = result.find_element(By.XPATH, "./div/a/p").text
    result_author = result.find_element(By.XPATH, "./div/div/a[@class='ArtInfo_author__0W3GJ']").text
    result_rating = result.find_element(By.XPATH, "./div/div/div[@class='ArtRating_rating__ntve8'] | "
                                            "./div/div/div[@class='ArtRating_rating__ntve8 ArtRating_grey__3_ZvG']").text
    result_rating = float(result_rating.replace(",", "."))
    result_url = result.find_element(By.XPATH, "./div/a").get_attribute("href")
    result_data.append([result_title, result_author, result_rating, result_url])
    #result_data.append({"title": result_title, "author": result_author, "rating": result_rating, "url": result_url})

# Запись данных в файл CSV
with open("books.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["title", "author", "rating", "url"])
    writer.writerows(result_data)


# Запись данных в файл JSON
with open('movies.json', 'w') as file:
   json.dump(result_data, file)

driver.close()



"""
while True:
    time.sleep(4)
    # Ожидаем появление объекта (html код) карточек товара
    results = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='ArtV2Default_cover__text__k3N4V']")))


    # Прокручиваем страницу выполняя JAVA Script
    driver.execute_script('window.scrollBy(0, 1800)')
    time.sleep(2)
        
    # Извлечение информации каждой книги
    for result in results:
        result_title = result.find_element(By.XPATH, "./div/a/p").text
        result_author = result.find_element(By.XPATH, "./div/div/a[@class='ArtInfo_author__0W3GJ']").text
        result_rating = result.find_element(By.XPATH, "./div/div/div[@class='ArtRating_rating__ntve8'] | "
                                            "./div/div/div[@class='ArtRating_rating__ntve8 ArtRating_grey__3_ZvG']").text
        result_rating = float(result_rating.replace(",", "."))
        result_url = result.find_element(By.XPATH, "./div/a").get_attribute("href")
        result_data.append([result_title, result_author, result_rating, result_url])
        #result_data.append({"title": result_title, "author": result_author, "rating": result_rating, "url": result_url})
    
    # Проверяем есть ли кнопка дальше
    try:
        next = driver.find_element(By.XPATH,  "//div[@class='PaginatedContent_pages__B9Lnu']/button")
        next.click()
    except Exception:
        break
"""

