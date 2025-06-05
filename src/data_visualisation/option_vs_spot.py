import numpy as np
import matplotlib.pyplot as plt
from calculations.optionPrice import *
import seaborn as sns
import mplcursors

def plot_option_pnl(K, option_price, option_type):
    """
    Genera un gráfico que compara el P&L de comprar una opción (call/put) vs. comprar/vender en spot.
    
    :param K: Precio de ejercicio de la opción
    :param option_price: Precio pagado por la opción
    :param option_type: "call" o "put"
    """
    # Definir el rango de precios del subyacente
    prices = np.arange(K - 5, K + 6, 1)
    
    # Calcular el P&L de la opción
    if option_type == "call":
        option_pnl = np.maximum(prices - K, 0) - option_price
        spot_pnl = prices - K  # Comprar en spot
        legend_spot = "Compra Spot"
    elif option_type == "put":
        option_pnl = np.maximum(K - prices, 0) - option_price
        spot_pnl = K - prices  # Short en spot
        legend_spot = "Venta Spot"
    else:
        raise ValueError("El tipo de opción debe ser 'call' o 'put'")
    
    # Configurar estilo profesional
    sns.set_style("whitegrid")
    fig, ax = plt.subplots(figsize=(9, 6))
    line1, = ax.plot(prices, option_pnl, label=f"{option_type.capitalize()} P&L", linestyle='-', linewidth=2, marker='o', color='#1f77b4')
    line2, = ax.plot(prices, spot_pnl, label=f"{legend_spot} P&L", linestyle='--', linewidth=2, marker='s', color='#ff7f0e')
    
    # Agregar títulos y etiquetas
    ax.axhline(0, color='black', linewidth=1, linestyle='--', alpha=0.7)
    ax.axvline(K, color='gray', linewidth=1, linestyle='--', alpha=0.7, label="Strike Price")
    ax.set_xlabel("Precio del Subyacente", fontsize=12, fontweight='bold')
    ax.set_ylabel("P&L", fontsize=12, fontweight='bold')
    ax.set_title(f"Comparación P&L: {option_type.capitalize()} vs. {legend_spot}", fontsize=14, fontweight='bold')
    
    # Ajustar leyenda
    ax.legend(fontsize=11, loc='best', frameon=True, edgecolor='black')
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.set_xticks(prices)  # Mostrar valores 1 a 1 en el eje x
    
    # Agregar etiquetas emergentes interactivas con fondo blanco y primer valor con 2 decimales
    cursor = mplcursors.cursor([line1, line2], hover=True)
    cursor.connect("add", lambda sel: sel.annotation.set_text(f"({sel.target[0]:.2f}, {sel.target[1]:.2f})"))
    cursor.connect("add", lambda sel: sel.annotation.get_bbox_patch().set_facecolor("white"))
    cursor.connect("add", lambda sel: sel.annotation.get_bbox_patch().set_alpha(1))
    
    plt.show()


def plot_roi_comparison(S, K, T_days, r, sigma, option_type, q=0, initial_option_price=None):
    prices = np.arange(K - 5, K + 6, 1)
    
    if option_type == 'call':
        # ROI para la posición larga en spot
        roi_spot = (prices - S) / S * 100
        spot_label = 'ROI Long Spot'
        
    else:  # put
        # ROI para la posición corta en spot
        roi_spot = (S - prices) / S * 100
        spot_label = 'ROI Short Spot'
    
    # ROI para la opción
    if initial_option_price is None:
        initial_option_price = calculate_option_price(S, K, T_days, r, sigma, option_type, q)
    
    option_prices = [calculate_option_price(p, K, T_days, r, sigma, option_type, q) for p in prices]
    
    if option_type == 'call':
        option_payoffs = np.maximum(prices - K, 0)
    else:  # put
        option_payoffs = np.maximum(K - prices, 0)
    
    roi_option = (option_payoffs - initial_option_price) / initial_option_price * 100
    
    # Configurar estilo profesional
    sns.set_style("whitegrid")
    fig, ax = plt.subplots(figsize=(9, 6))
    line1, = ax.plot(prices, roi_spot, label=spot_label, linestyle='--', linewidth=2, marker='s', color='#ff7f0e')
    line2, = ax.plot(prices, roi_option, label=f'ROI {option_type.capitalize()} Option', linestyle='-', linewidth=2, marker='o', color='#1f77b4')
    
    ax.axvline(x=K, color='gray', linestyle='--', linewidth=1, alpha=0.7, label='Strike')
    ax.axhline(y=0, color='black', linestyle='--', linewidth=1, alpha=0.7)
    
    ax.set_title(f'ROI Comparison: {"Long" if option_type == "call" else "Short"} Spot vs {option_type.capitalize()} Option', fontsize=14, fontweight='bold')
    ax.set_xlabel('Underlying Price', fontsize=12, fontweight='bold')
    ax.set_ylabel('ROI (%)', fontsize=12, fontweight='bold')
    
    ax.legend(fontsize=11, loc='best', frameon=True, edgecolor='black')
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.set_xticks(prices)
    
    # Agregar etiquetas emergentes interactivas con fondo blanco y primer valor con 2 decimales
    cursor = mplcursors.cursor([line1, line2], hover=True)
    cursor.connect("add", lambda sel: sel.annotation.set_text(f"({sel.target[0]:.2f}, {sel.target[1]:.2f})"))
    cursor.connect("add", lambda sel: sel.annotation.get_bbox_patch().set_facecolor("white"))
    cursor.connect("add", lambda sel: sel.annotation.get_bbox_patch().set_alpha(1))
    
    plt.show()


