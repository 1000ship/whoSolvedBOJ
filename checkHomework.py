import asyncio
import requests
from bs4 import BeautifulSoup, PageElement

class User (object):
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

async def getUserProblemHistory ( id ):
    res = requests.get(f"https://www.acmicpc.net/user/{id}")
    bs = BeautifulSoup(res.content, "html.parser")
    success_panel, fail_panel = bs.find_all("div", {"class":"panel"})
    success_body = success_panel.find("div", {"class":"panel-body"})
    success_spans = success_body.find_all("span", {"class", "problem_number"})
    success_numbers = [ int(item.text) for item in success_spans ] # 성공한 문제 코드들
    fail_body = fail_panel.find("div", {"class":"panel-body"})
    fail_spans = fail_body.find_all("span", {"class", "problem_number"})
    fail_numbers = [ int(item.text) for item in fail_spans ] # 실패한 문제 코드들
    print( f"{id} loaded" )
    return (success_numbers, fail_numbers)

async def getUserDict ( ids ):
    historyDict = {}
    futures = [ asyncio.ensure_future(getUserProblemHistory(id)) for id in ids]
    result = await asyncio.gather( *futures )
    for i in range(len(ids)):
        historyDict[ids[i]] = User( *result[i] )
    return historyDict

async def main ():
    ids = ["cjstjdgur123", "baekjoon", "test"]
    userDict = await getUserDict( ids )

    print()
    homeworkCode = 1001
    print( f"homework code is {homeworkCode}" )
    for user in userDict:
        didSuccess = userDict[user].didSuccess( homeworkCode )
        if didSuccess:
            print( f"{user} did homework" )
        else:
            print( f"{user} didn't homework" )

asyncio.get_event_loop().run_until_complete( main() )