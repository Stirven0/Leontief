import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv('datos_impacto.csv', index_col=0)
    print("=== DATOS ORIGINALES ===")
    print(df)
    print()

    flujos = df.loc[['agricultura', 'tecnologia', 'servicios'], ['agricultura', 'tecnologia', 'servicios']].values
    produccion_total = df.loc['produccion_total', ['agricultura', 'tecnologia', 'servicios']].values
    demanda_original = df.loc[['agricultura', 'tecnologia', 'servicios'], 'demanda_final'].values

    A = flujos / produccion_total
    I = np.eye(3)
    L = np.linalg.inv(I - A)

    produccion_original = L @ demanda_original

    demanda_nueva = demanda_original.copy()
    demanda_nueva[0] *= 1.20

    produccion_nueva = L @ demanda_nueva

    sectores = ['Agricultura', 'Tecnologia', 'Servicios']

    print("=== IMPACTO DEL AUMENTO DEL 20% EN DEMANDA DE AGRICULTURA ===")
    print()
    print("Demanda final original vs nueva:")
    for i, sector in enumerate(sectores):
        print(f"{sector}: {demanda_original[i]:.2f} -> {demanda_nueva[i]:.2f}")
    print()

    print("Produccion total requerida (original vs nueva):")
    for i, sector in enumerate(sectores):
        cambio = produccion_nueva[i] - produccion_original[i]
        cambio_pct = (cambio / produccion_original[i]) * 100
        print(f"{sector}: {produccion_original[i]:.2f} -> {produccion_nueva[i]:.2f} (cambio: {cambio:+.2f}, {cambio_pct:+.1f}%)")
    print()

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    ax1 = axes[0]
    x_pos = np.arange(len(sectores))
    width = 0.35
    ax1.bar(x_pos - width/2, produccion_original, width, label='Produccion Original', color='steelblue')
    ax1.bar(x_pos + width/2, produccion_nueva, width, label='Produccion con +20% Demanda Agricultura', color='coral')
    ax1.set_xlabel('Sector')
    ax1.set_ylabel('Miles de millones de pesos')
    ax1.set_title('Impacto del Aumento del 20% en Demanda de Agricultura')
    ax1.set_xticks(x_pos)
    ax1.set_xticklabels(sectores)
    ax1.legend()
    ax1.grid(axis='y', alpha=0.3)

    ax2 = axes[1]
    cambios_pct = [(produccion_nueva[i] - produccion_original[i]) / produccion_original[i] * 100 for i in range(len(sectores))]
    colores = ['#2ecc71' if c > 0 else '#e74c3c' for c in cambios_pct]
    ax2.bar(sectores, cambios_pct, color=colores)
    ax2.set_xlabel('Sector')
    ax2.set_ylabel('Cambio porcentual (%)')
    ax2.set_title('Cambio Porcentual en Produccion por Sector')
    ax2.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    ax2.grid(axis='y', alpha=0.3)

    plt.tight_layout()
    plt.savefig('resultados_impacto.png', dpi=150, bbox_inches='tight')
    print("Grafico guardado como 'resultados_impacto.png'")

    with open('resultados.txt', 'w') as f:
        f.write("=== IMPACTO DEL AUMENTO DEL 20% EN DEMANDA DE AGRICULTURA ===\n\n")
        f.write("Demanda final original vs nueva:\n")
        for i, sector in enumerate(sectores):
            f.write(f"{sector}: {demanda_original[i]:.2f} -> {demanda_nueva[i]:.2f}\n")
        f.write("\nProduccion total requerida (original vs nueva):\n")
        for i, sector in enumerate(sectores):
            cambio = produccion_nueva[i] - produccion_original[i]
            cambio_pct = (cambio / produccion_original[i]) * 100
            f.write(f"{sector}: {produccion_original[i]:.2f} -> {produccion_nueva[i]:.2f} (cambio: {cambio:+.2f}, {cambio_pct:+.1f}%)\n")
    print("Resultados guardados en 'resultados.txt'")

if __name__ == '__main__':
    main()
