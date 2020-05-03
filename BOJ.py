import asyncio
import requests
from bs4 import BeautifulSoup, PageElement
import datetime
import EnumerationBOJ

class Student():
    def __init__(self, name, id):
        self.name = name;
        self.id = id;
        self.successList = None
        self.failList = None
    def __str__(self):
        return f"({self.name}, {self.id})"
    def loadSuccessFail (self):
        res = requests.get(f"https://www.acmicpc.net/user/{self.id}")
        bs = BeautifulSoup(res.content, "html.parser")
        success_panel, fail_panel = bs.find_all("div", {"class": "panel"})
        success_body = success_panel.find("div", {"class": "panel-body"})
        success_spans = success_body.find_all("span", {"class", "problem_number"})
        success_numbers = [int(item.text) for item in success_spans]  # 성공한 문제 코드들
        fail_body = fail_panel.find("div", {"class": "panel-body"})
        fail_spans = fail_body.find_all("span", {"class", "problem_number"})
        fail_numbers = [int(item.text) for item in fail_spans]  # 실패한 문제 코드들
        # print(f"{self.id}.loadSuccessFail loaded") # for debugging
        self.successList = success_numbers
        self.failList = fail_numbers
    def didSuccess (self, problemId):
        if not self.successList:
            self.loadSuccessFail()
        return problemId in self.successList
    def didFail (self, problemId):
        if not self.failList:
            self.loadSuccessFail()
        return problemId in self.failList

def getStudents ():
    students = []
    f = open("students.txt", 'r', -1, 'utf-8')
    for line in f.readlines():
        str = line.strip()
        arr = str.split()
        if arr[0] == 'end':
            break
        students += [Student(arr[0], arr[1])]
    f.close()
    return students

def getHomeworkCodes ():
    homeworkCodeFile = open("homeworkCodes.txt", "r", -1, 'utf-8')
    homeworkCodes = [ int(code.strip()) for code in homeworkCodeFile.readlines() ]
    return homeworkCodes