import requests
import json

dic_of_advice = {}
lst_of_advice = []


def check_available(item, lst):
   if item in lst:
      res = requests.get('https://api.adviceslip.com/advice')
      res_json = res.json()
      advice = res_json['slip']['advice']
      check_available(advice, lst)
   else:
      lst.append(item)
   return lst
      
for i in range(200):
    res = requests.get('https://api.adviceslip.com/advice')
    res_json = res.json()
    advice = res_json['slip']['advice']
    check_available(advice, lst_of_advice)

count = 0
for advice in lst_of_advice:
   dic_of_advice[str(count)] = advice
   count+= 1

with open('advice.txt', 'w') as advice_txt:
   for advice in dic_of_advice:
      advice_txt.write(f"{advice} | {dic_of_advice[advice]}\n")
