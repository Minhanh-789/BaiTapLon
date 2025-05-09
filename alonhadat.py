import time
import csv
import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

def scrape_alonhadat():
    options = Options()
    options.headless = False  # Đặt True nếu muốn chạy ẩn
    driver = webdriver.Chrome(options=options)

    driver.get("https://alonhadat.com.vn/nha-dat/can-ban/biet-thu-nha-lien-ke/3/da-nang.html")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "content-item"))
    )

    data = []
    page = 1

    while True:
        print(f" Đang xử lý trang {page}...")

        listings = driver.find_elements(By.CSS_SELECTOR, "div.content-item")

        for listing in listings:
            try:
                title = listing.find_element(By.CSS_SELECTOR, "div.ct_title a").text.strip()
            except:
                title = "N/A"

            try:
                description = listing.find_element(By.CSS_SELECTOR, "div.ct_description").text.strip()
            except:
                description = "N/A"

            try:
                address = listing.find_element(By.CSS_SELECTOR, "div.ct_address").text.strip()
            except:
                address = "N/A"

            try:
                price = listing.find_element(By.CSS_SELECTOR, "div.price").text.strip()
            except:
                price = "N/A"

            data.append([title, description, address, price])

        try:
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//a[@class="Next"]'))
            )
            if 'href' in next_button.get_attribute('outerHTML'):
                next_button.click()
                page += 1
                time.sleep(2)
            else:
                break
        except:
            print(" Không còn trang tiếp theo.")
            break

    with open("alonhadat_bietthu_danang.csv", "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow(["Tiêu đề", "Mô tả", "Địa chỉ", "Giá"])
        writer.writerows(data)

    print(f" Đã lưu {len(data)} mục vào file CSV.")
    driver.quit()

    # Dừng chương trình sau khi hoàn thành
    sys.exit() 

# lịch chạy tự động lúc 6h sáng
schedule.every().day.at("06:00").do(scrape_alonhadat)

# Vòng lặp chạy liên tục để canh giờ
if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(60)  

