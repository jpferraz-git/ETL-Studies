import matplotlib.pyplot as plt

# Valor de exemplo vindo da medida percentMigrated
percent_migrated = 88  # substitua pelo valor real

fig, ax = plt.subplots(figsize=(6, 2.5))
ax.barh(['Migrated'], [percent_migrated], height=0.5)
ax.set_xlim(0, 100)
ax.set_xlabel('Percentual (%)')
ax.set_title('KPI – Percentual Migrado')
ax.set_yticks([])  # esconde o eixo Y
ax.text(
    percent_migrated / 2, 0,
    f'{percent_migrated} %',
    ha='center', va='center',
    fontsize=14, weight='bold',
    color='white'
)
plt.tight_layout()
plt.show()