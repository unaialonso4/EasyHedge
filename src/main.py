from data_ingestion.data_provider import get_stock_price, get_time_to_expiry, get_risk_free_rate
from calculations.greeks import *

if __name__ == "__main__":
    # Parámetros de ejemplo
    ticker = "AMP.MC"  # Ticker del activo subyacente
    expiry_date = "2025-06-01"  # Fecha de vencimiento
    
    print("=== Probar métodos de data_provider.py ===")
    
    # Obtener el precio del activo subyacente
    try:
        stock_price = get_stock_price(ticker)
        print(f"Precio del activo subyacente ({ticker}): {stock_price}\n")
    except Exception as e:
        print(f"Error al obtener el precio del activo subyacente: {e}\n")

    
    # Calcular el tiempo hasta el vencimiento
    try:
        time_to_expiry = get_time_to_expiry(expiry_date)
        print(f"Tiempo hasta vencimiento ({expiry_date}): {time_to_expiry:.2f} días\n")
    except Exception as e:
        print(f"Error al calcular el tiempo hasta el vencimiento: {e}\n")
    

    # Obtener la tasa de interés libre de riesgo
    try:
        risk_free_rate = get_risk_free_rate()
        print(f"Tasa de interés libre de riesgo (fijo): {risk_free_rate:.2%}")
    except Exception as e:
        print(f"Error al obtener la tasa de interés libre de riesgo: {e}")

    # Calcular delta
    try:
        delta = calculate_delta(100,95,time_to_expiry,risk_free_rate,0.2,"put")
        print(f"La delta de tu opción es: {delta:.4f}")
    except Exception as e:
        print(f"Error al obtener la delta: {e}")