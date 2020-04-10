import pyautogui
import time
import os.path
import win32com.client 
from os import walk
import os
from tkinter import Tk
import webbrowser
import sys

pyautogui.FAILSAFE = True

time.sleep(2)
all_folders = os.path.join("downloads")
absPath=os.path.abspath(all_folders)
def makeText(store):
    webName= store.replace(' ', '-').lower()
    print(webName)
    openExcelFun=win32com.client.Dispatch('Excel.Application')
    openExcelFun.visible=1
    pathExcel=absPath+"/"+store+ "/"+ webName+ "-calories-per-dollar.xlsx"
    wb1=openExcelFun.Workbooks.open(pathExcel)
    time.sleep(5)
    #Select excel Text
    pyautogui.hotkey("ctrl","a")
    pyautogui.hotkey("ctrl","c")
    time.sleep(3)
    #open Chrome tableizer
    url = 'http://tableizer.journalistopia.com/'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    time.sleep(2)
    corner=pyautogui.locateCenterOnScreen('corner_tabelizer.png')
    pyautogui.click(corner, duration=0.1) 
    pyautogui.hotkey("ctrl","v")
    sub=pyautogui.locateCenterOnScreen('submit_tabelizer.PNG')
    pyautogui.click(sub, duration=0.1)
    time.sleep(2)
    result=pyautogui.locateCenterOnScreen('result_tabelizer.png')
    pyautogui.click(result, duration=0.1)
    pyautogui.hotkey("ctrl","c")
    time.sleep(5)
    #text is coppied to clipboard

makeText(restaurant)

clipboardData = Tk()
data = clipboardData.selection_get(selection = "CLIPBOARD") 


startData=data.find("/thead")+7
dataSecond=data[startData:]
dataHeader='''
<div style="overflow-x:auto;">
<table id="myTable" table class ="sortable">

   <colgroup>
    <col class="white" />
    <col class="white" />
    <col class="green" />
    <col class="red" />
    <col class="white" />
    <col class="white" />
    <col class="white" />

  </colgroup>

  <thead>
  <tr >
   <!--When a header is clicked, run the sortTable function, with a parameter, 0 for sorting by names, 1 for sorting by country:-->  
  <th>Menu Item</th>
  <th>Before Tax Price </th>
  <th >Calories Per Dollar</th>
  <th>Protein Per Dollar</th>
  <th>Cost If  Eaten All Year</th>
  <th>Calories</th>
  <th>Protein</th>
  </tr>
</thead>
'''
dataTotal=dataHeader+dataSecond



def autoArticle(name, table):
    webName= name.replace(' ', '-').lower()
    pyautogui.typewrite(name + " Calories Per Dollar and Protein Per Dollar", interval=0.01)
    pyautogui.hotkey('tab')
    headerPhoto= '''<img class="EfficiencyHeaderPhoto" src="/images/headers/'''+webName+'''-header.jpg">'''
    pyautogui.typewrite("<h2> Save Money At " + name + '</h2> \n <ul><li>The Highest Calories Per Dollar Item is </li><li>The Highest Protein Per Dollar Item is </li><li>The Efficieny Recommendation is </li></ul> \n' + table +''' <h2>Cheapest Food</h2> \n thats still almost 2x more than we spend on homecooked food. Most menu items were around 150-250 calories per dollar, 4x more expensive than eating at home. \n Use math to eat healthy and low cost<a href="https://efficiencyiseverything.com/food/"> Efficiently</a> for $1,000/year. \n [email]''', interval=0.01)
    

#start wordpress
url = "https://efficiencyiseverything.com/wordpress/wp-admin/post-new.php?post_type=page"
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open(url)

time.sleep(5)



restaurant="Starbucks"


autoArticle(restaurant, dataTotal)

