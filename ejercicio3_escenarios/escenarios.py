import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv('datos_escenarios.csv', index_col=0)
    print("=== DATOS ORIGINALES ===")
    print(df)
    print()

    flujos = df.loc[['agricultura', 'tecnologia', 'servicios'], ['agricultura', 'tecnologia', 'servicios']].values
    produccion_total = df.loc['produccion_total', ['agricultura', 'tecnologia', 'servicios']].values
    demanda_base = df.loc[['agricultura', 'tecnologia', 'servicios'], 'demanda_final'].values

    A = flujos / produccion_total
    I = np.eye(3)
    L = np.linalg.inv(I - A)

    demanda_conservadora = demanda_base * 0.90
    demanda_optimista = demanda_base * 1.15

    produccion_conservadora = L @ demanda_conservadora
    produccion_base = L @ demanda_base
    produccion_optimista = L @ demanda_optimista

    sectores = ['Agricultura', 'Tecnologia', 'Servicios']

    print("=== COMPARACION DE ESCENARIOS DE DEMANDA FINAL ===")
    print()
    print("Demanda final por escenario:")
    for i, sector in enumerate(sectores):
        print(f"{sector}:")
        print(f"  Conservador (-10%): {demanda_conservadora[i]:.2f}")
        print(f"  Base: {demanda_base[i]:.2f}")
        print(f"  Optimista (+15%): {demanda_optimista[i]:.2f}")
    print()

    print("Produccion total requerida por escenario:")
    for i, sector in enumerate(sectores):
        print(f"{sector}:")
        print(f"  Conservador: {produccion_conservadora[i]:.2f}")
        print(f"  Base: {produccion_base[i]:.2f}")
        print(f"  Optimista: {produccion_optimista[i]:.2f}")
    print()

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    ax1 = axes[0]
    x_pos = np.arange(len(sectores))
    width = 0.25
    ax1.bar(x_pos - width, produccion_conservadora, width, label='Conservador (-10%)', color='#e74c3c')
    ax1.bar(x_pos, produccion_base, width, label='Base', color='#3498db')
    ax1.bar(x_pos + width, produccion_optimista, width, label='Optimista (+15%)', color='#2ecc71')
    ax1.set_xlabel('Sector')
    ax1.set_ylabel('Miles de millones de pesos')
    ax1.set_title('Produccion Total Requerida por Escenario')
    ax1.set_xticks(x_pos)
    ax1.set_xticklabels(sectores)
    ax1.legend()
    ax1.grid(axis='y', alpha=0.3)

    ax2 = axes[1]
    cambios_conservador = [(produccion_conservadora[i] - produccion_base[i]) / produccion_base[i] * 100 for i in range(len(sectores))]
    cambios_optimista = [(produccion_optimista[i] - produccion_base[i]) / produccion_base[i] * 100 for i in range(len(sectores))]

    x_pos2 = np.arange(len(sectores))
    width2 = 0.35
    ax2.bar(x_pos2 - width2/2, cambios_conservador, width2, label='Conservador vs Base', color='#e74c3c')
    ax2.bar(x_pos2 + width2/2, cambios_optimista, width2, label='Optimista vs Base', color='#2ecc71')
    ax2.set_xlabel('Sector')
    ax2.set_ylabel('Cambio porcentual (%)')
    ax2.set_title('Variacion Porcentual respecto al Escenario Base')
    ax2.set_xticks(x_pos2)
    ax2.set_xticklabels(sectores)
    ax2.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    ax2.legend()
    ax2.grid(axis='y', alpha=0.3)

    plt.tight_layout()
    plt.savefig('resultados_escenarios.png', dpi=150, bbox_inches='tight')
    print("Grafico guardado como 'resultados_escenarios.png'")

    with open('resultados.txt', 'w') as f:
        f.write("=== COMPARACION DE ESCENARIOS DE DEMANDA FINAL ===\n\n")
        f.write("Demanda final por escenario:\n")
        for i, sector in enumerate(sectores):
            f.write(f"{sector}:\n")
            f.write(f"  Conservador (-10%): {demanda_conservadora[i]:.2f}\n")
            f.write(f"  Base: {demanda_base[i]:.2f}\n")
            f.write(f"  Optimista (+15%): {demanda_optimista[i]:.2f}\n")
        f.write("\nProduccion total requerida por escenario:\n")
        for i, sector in enumerate(sectores):
            f.write(f"{sector}:\n")
            f.write(f"  Conservador: {produccion_conservadora[i]:.2f}\n")
            f.write(f"  Base: {produccion_base[i]:.2f}\n")
            f.write(f"  Optimista: {produccion_optimista[i]:.2f}\n")
    print("Resultados guardados en 'resultados.txt'")

if __name__ == '__main__':
    main()
