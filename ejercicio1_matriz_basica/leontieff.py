import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    df = pd.read_csv('datos_guajira.csv', index_col=0)
    print("=== DATOS DE LA GUAJIRA ===")
    print(df)
    print()

    flujos = df.loc[['agricultura', 'tecnologia', 'servicios'], ['agricultura', 'tecnologia', 'servicios']].values
    produccion_total = df.loc['produccion_total', ['agricultura', 'tecnologia', 'servicios']].values
    demanda_final = df.loc[['agricultura', 'tecnologia', 'servicios'], 'demanda_final'].values

    A = flujos / produccion_total
    print("=== MATRIZ DE COEFICIENTES TECNICOS (A) ===")
    print(pd.DataFrame(A, index=['Agricultura', 'Tecnologia', 'Servicios'],
                       columns=['Agricultura', 'Tecnologia', 'Servicios']))
    print()

    I = np.eye(3)
    IA = I - A
    print("=== MATRIZ (I - A) ===")
    print(pd.DataFrame(IA, index=['Agricultura', 'Tecnologia', 'Servicios'],
                       columns=['Agricultura', 'Tecnologia', 'Servicios']))
    print()

    L = np.linalg.inv(IA)
    print("=== MATRIZ INVERSA DE LEONTIEF (I - A)^-1 ===")
    print(pd.DataFrame(L, index=['Agricultura', 'Tecnologia', 'Servicios'],
                       columns=['Agricultura', 'Tecnologia', 'Servicios']))
    print()

    X = L @ demanda_final
    print("=== PRODUCCION TOTAL REQUERIDA (X) ===")
    for sector, prod in zip(['Agricultura', 'Tecnologia', 'Servicios'], X):
        print(f"{sector}: {prod:.2f} miles de millones de pesos")
    print()

    multiplicadores = L.sum(axis=0)
    print("=== MULTIPLICADORES DE PRODUCCION ===")
    for sector, mult in zip(['Agricultura', 'Tecnologia', 'Servicios'], multiplicadores):
        print(f"{sector}: {mult:.2f}")
    print()

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    ax1 = axes[0, 0]
    sectores = ['Agricultura', 'Tecnologia', 'Servicios']
    x_pos = np.arange(len(sectores))
    width = 0.35
    ax1.bar(x_pos - width/2, produccion_total, width, label='Produccion Total', color='steelblue')
    ax1.bar(x_pos + width/2, X, width, label='Produccion Requerida', color='coral')
    ax1.set_xlabel('Sector')
    ax1.set_ylabel('Miles de millones de pesos')
    ax1.set_title('Produccion Total vs Produccion Requerida por Sector')
    ax1.set_xticks(x_pos)
    ax1.set_xticklabels(sectores)
    ax1.legend()
    ax1.grid(axis='y', alpha=0.3)

    ax2 = axes[0, 1]
    sns.heatmap(A, annot=True, fmt='.3f', cmap='YlOrRd', ax=ax2,
                xticklabels=sectores, yticklabels=sectores)
    ax2.set_title('Matriz de Coeficientes Tecnicos (A)')

    ax3 = axes[1, 0]
    sns.heatmap(L, annot=True, fmt='.3f', cmap='YlGnBu', ax=ax3,
                xticklabels=sectores, yticklabels=sectores)
    ax3.set_title('Matriz Inversa de Leontief (I-A)^-1')

    ax4 = axes[1, 1]
    ax4.bar(sectores, multiplicadores, color=['#2ecc71', '#3498db', '#9b59b6'])
    ax4.set_xlabel('Sector')
    ax4.set_ylabel('Multiplicador')
    ax4.set_title('Multiplicadores de Produccion por Sector')
    ax4.grid(axis='y', alpha=0.3)

    plt.tight_layout()
    plt.savefig('resultados_leontieff.png', dpi=150, bbox_inches='tight')
    print("Grafico guardado como 'resultados_leontieff.png'")

    with open('resultados.txt', 'w') as f:
        f.write("=== RESULTADOS DE LA MATRIZ DE LEONTIEF - LA GUAJIRA ===\n\n")
        f.write("Matriz de Coeficientes Tecnicos (A):\n")
        f.write(pd.DataFrame(A, index=sectores, columns=sectores).to_string())
        f.write("\n\nMatriz Inversa de Leontief (I-A)^-1:\n")
        f.write(pd.DataFrame(L, index=sectores, columns=sectores).to_string())
        f.write("\n\nProduccion Total Requerida (X):\n")
        for sector, prod in zip(sectores, X):
            f.write(f"{sector}: {prod:.2f} miles de millones de pesos\n")
        f.write("\nMultiplicadores de Produccion:\n")
        for sector, mult in zip(sectores, multiplicadores):
            f.write(f"{sector}: {mult:.2f}\n")
    print("Resultados guardados en 'resultados.txt'")

if __name__ == '__main__':
    main()
