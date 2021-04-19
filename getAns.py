from selenium import webdriver
import difflib
import unittest

browser = webdriver.Chrome()

ansSheet = {
    "DemoKey": "DemoAns"
}


def choice_ans():
    try:
        browser.find_element_by_id("radio0").click()
    except:
        browser.find_element_by_id("trueAnswer").click()
    finally:
        browser.find_element_by_id("next").click()


def record():
    if "判斷題" in browser.find_element_by_id("analysisLogo").text:
        ansSheet[browser.find_element_by_id("intitle").text] = browser.find_element_by_class_name("right").text
    else:
        ansSheet[browser.find_element_by_id("intitle").text] = browser.find_element_by_class_name("right").text[3:]
    browser.find_element_by_id("nextAnalysis").click()


def getMatch():
    list = []
    type = browser.find_element_by_id("exericeLogo").text
    if "單選題" in type:
        print("單選")
        list.append(browser.find_element_by_id("radio0").text)
        list.append(browser.find_element_by_id("radio1").text)
        list.append(browser.find_element_by_id("radio2").text)
        list.append(browser.find_element_by_id("radio3").text)
        print(list)
    else:
        print("是非")
        ans = ansSheet.get(browser.find_element_by_id("_title").text)
        if "對" in ans:
            browser.find_element_by_id("trueAnswer").click()
        else:
            browser.find_element_by_id("falseAnswer").click()


def writeFile():
    key = open('dictkey.txt', 'w',encoding="utf-8")
    value = open('dictvalue.txt', 'w', encoding="utf-8")
    for k,v in ansSheet.items():
        key.write(str(k)+"\n")
        value.write(str(v)+"\n")
    key.close()
    value.close()


if __name__ == "__main__":
    browser.get('https://www.lawmatch.net/basicLaw/frontend/public/exercise.html?type=SEQUENCE')
    for i in range(330):
        choice_ans()
    browser.find_element_by_id("trueAnswer").click()
    browser.find_element_by_id("end").click()
    browser.find_element_by_id("errorAnalysis").click()
    # 已進入錯題界面
    for i in range(330):
        record()
    ansSheet[browser.find_element_by_id("intitle").text] = browser.find_element_by_class_name("right").text
    writeFile()
    print(ansSheet)

#trueAnswer


