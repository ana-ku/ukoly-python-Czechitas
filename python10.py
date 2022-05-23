import pandas
import pytemperature
import requests

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/temperature.csv")
open("temperatures.csv", "wb").write(r.content)
temperatures = pandas.read_csv('temperatures.csv').set_index("City")

print(temperatures.info())
# print(temperatures.iloc[:9])
# print(temperatures.loc["Prague"])

# print(temperatures[temperatures["AvgTemperature"] > 80])

# print(temperatures[(temperatures["AvgTemperature"] > 60) & (temperatures["Region"]=="Europe")])

# print(temperatures[(temperatures["AvgTemperature"] > 80) | (temperatures["AvgTemperature"] < -20)])


# BONUS

temperatures["AvgCelsius"] = pytemperature.f2c(temperatures["AvgTemperature"])
# print(temperatures.iloc[:9])
# print(temperatures[temperatures["AvgCelsius"] > 30])

# print(temperatures[(temperatures["AvgCelsius"] > 15) & (temperatures["Region"]=="Europe")])

# print(temperatures[(temperatures["AvgCelsius"] > 80) | (temperatures["AvgCelsius"] < -10)])

# print(temperatures[temperatures["Day"]==13])

usteploty = temperatures[(temperatures["Day"]==13) & (temperatures["Country"]=="US")]

usteploty.to_csv("export_dat.csv", sep=',', encoding='utf-8')
usteploty = pandas.read_csv('export_dat.csv')
print(usteploty[(usteploty["City"] == "Washington") | (usteploty["City"] == "Philadelphia")])
