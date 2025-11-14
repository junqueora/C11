import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose


air = pd.read_csv("airtravel.csv", index_col="Date", parse_dates=True)
air["Passengers"] = pd.to_numeric(air["Passengers"], errors="coerce")

plt.figure(figsize=(8,5))
plt.plot(air.index, air["Passengers"])
plt.title("AirTravel - Passageiros")
plt.xlabel("Tempo")
plt.ylabel("Passageiros")
plt.grid()
plt.show()

dec_air = seasonal_decompose(air["Passengers"], model="additive", period=12)
fig = dec_air.plot()
fig.set_size_inches(10,8)
plt.show()

co2 = pd.read_csv("co2_emissions.csv")

co2["Date"] = pd.to_datetime(co2["Year"], format="%Y")
co2 = co2.set_index("Date")
co2["CO2_Emissions"] = pd.to_numeric(co2["CO2_Emissions"], errors="coerce")

plt.figure(figsize=(8,5))
plt.plot(co2.index, co2["CO2_Emissions"])
plt.title("CO2 Emissions")
plt.xlabel("Ano")
plt.ylabel("Emissões")
plt.grid()
plt.show()

dec_co2 = seasonal_decompose(co2["CO2_Emissions"], model="additive", period=12)
fig = dec_co2.plot()
fig.set_size_inches(10,8)
plt.show()
