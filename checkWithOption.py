import asyncio
import requests
from bs4 import BeautifulSoup, PageElement
import datetime
import BOJ
from selenium import webdriver
from EnumerationBOJ import ResultID, LanguageID
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("driver/chromedriver")

def callQuery( userId, problemId, resultId, languageId):
    global driver
    driver.get( f"https://www.acmicpc.net/status?problem_id={problemId}&user_id={userId}&language_id={languageId.value}&result_id={resultId.value}&from_problem=1")
    try:
        while True:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "real-time-update"))
            )
            bs = BeautifulSoup(driver.page_source, "html.parser")
            a_tags = bs.find("a", {"class", "real-time-update"})
            str = a_tags.attrs["title"] or a_tags.attrs["data-original-title"]
            if not str:
                input(f"NO-DATA ERROR : {str}") # 절대로 실행 안되길 바람
                continue
            else:
                break
        string_timestamps = list(map( lambda x: x.attrs["title"] or x.attrs["data-original-title"], bs.find_all("a", {"class", "real-time-update"})))
        timestamps = list(map( lambda x: datetime.datetime.strptime(x, "%Y년 %m월 %d일 %H시 %M분 %S초"), string_timestamps ))
        # print(f"https://www.acmicpc.net/status?problem_id={problemId}&user_id={userId}&language_id={languageId.value}&result_id={resultId.value}&from_problem=1")
    except:
        print("Error in callQuery")
    expiry_datetime = datetime.datetime.strptime("2020년 5월 3일 0시 0분 0초", "%Y년 %m월 %d일 %H시 %M분 %S초")
    for dt in timestamps:
        if dt < expiry_datetime:
            return True
    else:
        return False

async def main():
    students = BOJ.getStudents()
    homeworkCodes = BOJ.getHomeworkCodes()

    csv = open("result.csv", "w");

    # print status and data on log and csv files
    print(f"{len(students)} students find")
    print("Current Time : {}".format(datetime.datetime.now()))
    print("{:22}".format("Name(ID)"), end="")
    print("{}".format("Name,ID,"), end="", file=csv)
    for code in homeworkCodes:
        print("{:>10}".format(f"{code}"), end=",")
        print(f"{code}", end=",", file=csv)
    print()
    print(file=csv)
    for student in students:
        print("{:20}".format(f"{student.name}({student.id})"), end="")
        print(f"{student.name},{student.id},", end="", file=csv)
        for code in homeworkCodes:
            didSuccess = student.didSuccess(code)
            if didSuccess:
                expirySuccess = callQuery(student.id, code, ResultID.SUCCESS, LanguageID.Python3)
                if expirySuccess:
                    print("{:>10}".format("⭕️"), end=",")
                    print("⭕", end=",", file=csv)
                else:
                    print("{:>10}".format("❗️️"), end=",")
                    print("❗️", end=",", file=csv)
            else:
                print("{:>9}".format("❌"), end=",")
                print("❌", end=",", file=csv)
        print()
        print(file=csv)
    csv.close()
    # end print

asyncio.get_event_loop().run_until_complete(main())
