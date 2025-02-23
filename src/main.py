from data_ingestion.data_provider import *
from calculations.greeks import *
from utils.operations import *
from calculations.volatility import *
from data_visualisation.option_vs_spot import *
from calculations.optionPrice import *

if __name__ == "__main__":
    # Parámetros de ejemplo
    ticker = "AAPL"  # Ticker del activo subyacente
    expiry_date = "2025-03-30"  # Fecha de vencimiento

market_price = 2.48766
P = 100
S = 100
T_days = 30
r = 0.05
v = 0.2333
option_type = "call"
q=0.15


"""
print("SENSIBILIDADES")

print("delta: " + str(calculate_delta(P, S, T_days, r,v,option_type)))
print("gamma: " + str(calculate_gamma(P, S, T_days, r,v)))
print("vega: " + str(calculate_vega(P, S, T_days, r,v)))
print("theta: " + str(calculate_theta(P, S, T_days, r,v,option_type)))
print("rho: " + str(calculate_rho(P, S, T_days, r,v, option_type)))



print("PRECIOS")
price = calculate_option_price(P, S, T_days, r, v, option_type, q)
print("PREMIUM AMERICAN: " + str(price))


print("VOLATILIDAD")
print(implied_volatility(2.48766, P, S, T_days, r, option_type, q))

price = calculate_option_price(P=150, S=100, T_days=30, r=0.05, sigma=0.233, option_type="put")
print(price)
pricec = calculate_option_price(P=50, S=100, T_days=30, r=0.05, sigma=0.233, option_type="call")
print(pricec)


# Ejemplo de uso
print("Precio con subya a 100: ")
print(calculate_option_price(P=100, S=100, T_days=30, r=0.05, sigma=0.20, option_type="call"))
print("Precio con subya a 110: ")
print(calculate_option_price(110, 100, 30, 0.05, 0.20, "call", 0.1))
"""
plot_roi_comparison(100, 100, 30, 0.05, 0.2, "call", 0)
