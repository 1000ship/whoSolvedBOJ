import asyncio
import requests
from bs4 import BeautifulSoup, PageElement
import datetime


class User(object):
    def __init__(self, success_list, fail_list):
        self.success_list = success_list
        self.fail_list = fail_list

    def __repr__(self):
        return f"{len(self.success_list)} sovled"

    def didSuccess(self, code):
        if code in self.success_list:
            return True
        return False

    def didFail(self, code):
        if code in self.fail_list:
            return True
        return False


async def getUserProblemHistory(id):
    res = requests.get(f"https://www.acmicpc.net/user/{id}")
    bs = BeautifulSoup(res.content, "html.parser")
    success_panel, fail_panel = bs.find_all("div", {"class": "panel"})
    success_body = success_panel.find("div", {"class": "panel-body"})
    success_spans = success_body.find_all("span", {"class", "problem_number"})
    success_numbers = [int(item.text) for item in success_spans]  # 성공한 문제 코드들
    fail_body = fail_panel.find("div", {"class": "panel-body"})
    fail_spans = fail_body.find_all("span", {"class", "problem_number"})
    fail_numbers = [int(item.text) for item in fail_spans]  # 실패한 문제 코드들
    print(f"{id} loaded")
    return (success_numbers, fail_numbers)


async def getUserDict(ids):
    historyDict = {}
    futures = [asyncio.ensure_future(getUserProblemHistory(id)) for id in ids]
    result = await asyncio.gather(*futures)
    for i in range(len(ids)):
        historyDict[ids[i]] = User(*result[i])
    return historyDict


async def main():
    nameDict = {}
    ids = []

    csv = open("result.csv", "w");

    f = open("students.txt", 'r', -1, 'utf-8')
    for line in f.readlines():
        str = line.strip()
        arr = str.split()
        if arr[0] == 'end':
            break
        nameDict[arr[1]] = arr[0]
        ids += [arr[1]]
    f.close()

    print(f"{len(ids)} students")
    # ids = ["cjstjdgur123", "baekjoon", "test"]
    userDict = await getUserDict(ids)

    print("Current Time : {}".format(datetime.datetime.now()))
    homeworkCodeFile = open("homeworkCodes.txt", "r", -1, 'utf-8')
    homeworkCodes = [ int(code.strip()) for code in homeworkCodeFile.readlines() ]
    print(homeworkCodes)
    print("{:22}".format("Name(ID)"), end="")
    print("{}".format("Name,ID,"), end="", file=csv)
    for code in homeworkCodes:
        print("{:>10}".format(f"{code}"), end=",")
        print(f"{code}", end=",", file=csv)
    print()
    print(file=csv)

    for user in userDict:
        print("{:20}".format(f"{nameDict[user]}({user})"), end="")
        print(f"{nameDict[user]},{user},", end="", file=csv)
        for code in homeworkCodes:
            didSuccess = userDict[user].didSuccess(code)
            if didSuccess:
                print("{:>10}".format("⭕️"), end=",")
                print("⭕", end=",", file=csv)
            else:
                print("{:>9}".format("❌"), end=",")
                print("❌", end=",", file=csv)
        print()
        print(file=csv)
    csv.close()

asyncio.get_event_loop().run_until_complete(main())
