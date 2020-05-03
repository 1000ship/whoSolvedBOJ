import asyncio
import requests
from bs4 import BeautifulSoup, PageElement
import datetime
import BOJ

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
                print("{:>10}".format("⭕️"), end=",")
                print("⭕", end=",", file=csv)
            else:
                print("{:>9}".format("❌"), end=",")
                print("❌", end=",", file=csv)
        print()
        print(file=csv)
    csv.close()
    # end print

asyncio.get_event_loop().run_until_complete(main())
