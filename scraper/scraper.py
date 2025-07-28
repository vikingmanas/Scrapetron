from selenium import webdriver
from selenium.webdriver import ChromeOptions as Options
from bs4 import BeautifulSoup

def scrape_site(url):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    data = []
    for item in soup.select(".your-target-class"): 
        title = item.get_text(strip=True)
        data.append({"title": title})

    driver.quit()
    return data
