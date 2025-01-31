from data_ingestion.data_provider import *
from calculations.greeks import *
from utils.operations import *

if __name__ == "__main__":
    # Parámetros de ejemplo
    ticker = "AAPL"  # Ticker del activo subyacente
    expiry_date = "2025-03-30"  # Fecha de vencimiento
    interestRate = 0.0431

print(get_time_to_expiry("2025-03-14"))
print(interestRate) 
print(get_time_to_expiry("2025-03-30"))
print(get_stock_price(ticker))

print("=== Probar métodos de data_provider.py ===")



print("delta: " + str(calculate_delta(get_stock_price(ticker), 250, get_time_to_expiry("2025-03-30"), interestRate,0.2,"put")))
print("gamma: " + str(calculate_gamma(get_stock_price(ticker), 250, get_time_to_expiry("2025-03-30"), interestRate,0.2)))
print("vega: " + str(calculate_vega(get_stock_price(ticker), 250, get_time_to_expiry("2025-03-30"), interestRate,0.2)))
print("theta: " + str(calculate_theta(get_stock_price(ticker), 250, get_time_to_expiry("2025-03-30"), interestRate,0.2,"put")))
print("rho: " + str(calculate_rho(get_stock_price(ticker), 250, get_time_to_expiry("2025-03-30"), interestRate,0.2, "put")))