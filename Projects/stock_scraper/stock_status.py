import xlutils
import pandas
from bs4 import BeautifulSoup
from urllib.request import urlopen

#url = "https://www.pythonforbeginners.com"
url = "https://www.marketwatch.com/investing/stock/fb/analystestimates"

#content = urlopen(url).read()
content = urlopen(url).read()

print(content)
soup = BeautifulSoup(content)

#test = soup.find_all("td")
test = soup.find_all("tr")
test = str(test)

#-----------------------Splitting BUY----------
test_split = test.split("BUY")

#test_split = test.split("<td class=")

#test_split = test.split("<td class=\"first\">")


print("\n\n\n"), #print("Buy\n\n\n")
#print(test_split[1])
test_buy = test_split[1]
test_buy = test_buy.split("\">")
test_buy = test_buy[1]
test_buy = test_buy.split("</td>")
test_buy = test_buy[0]
print("Analyst Recommendations")
print("BUY:            ", test_buy)
#print(test_buy)

#---------------------------Split Mean current
test_mean = test.split("MEAN")
test_mean = test_mean[1]
test_mean = test_mean.split("current\">")
test_mean = test_mean[1]
test_mean = test_mean.split("</td>")
test_mean = test_mean[0]
print("MEAN:           ", test_mean)
#print(test_mean)


#-------------------------Split Mean 3 Months
test_mean_3mo = test.split("MEAN")
test_mean_3mo = test_mean_3mo[1]
test_mean_3mo = test_mean_3mo.split("<td class=\"\">")
test_mean_3mo = test_mean_3mo[2]
test_mean_3mo = test_mean_3mo.split("</td>")
test_mean_3mo = test_mean_3mo[0]
print("MEAN 3 Months Ago: ", test_mean_3mo)
#print(test_mean_3mo)

#-----------------------Add to excel
#print(test_split[11])

#print(soup.find(text="buy"))

#print(soup.prettify())
