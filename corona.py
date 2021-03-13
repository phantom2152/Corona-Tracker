from covid import Covid
import pyfiglet
import pprint
covid = Covid()
print(pyfiglet.figlet_format("WELCOME TO WORLD COVID TRACKER", font="digital"))
country = str(input("Enetr The Country Name:"))
try:
    pp = covid.get_status_by_country_name(country)
except ValueError:
    print("Mentioned Coutry not found...")
    exit()
print("Country Name:"+str(pp['country']))
print("Confirmed Cases:"+str(pp['confirmed']))
print("Active Cases:" + str(pp['active']))
print("Deaths:"+str(pp['deaths']))
print("Recovered:"+str(pp['recovered']))
print(pyfiglet.figlet_format("WEAR MASK AND BE SAFE.....", font="slant"))
