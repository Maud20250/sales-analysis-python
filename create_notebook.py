import nbformat as nbf

nb = nbf.v4.new_notebook()

nb.cells = [
    nbf.v4.new_markdown_cell("# Sales Analysis Project\nAnalyse des ventes par produit, categorie et region."),
    nbf.v4.new_code_cell("""import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/sales_data.csv')
df['total_sales'] = df['quantity'] * df['unit_price']
print(df.head())
print(df.shape)"""),
    nbf.v4.new_code_cell("""category_sales = df.groupby('category')['total_sales'].sum()
print(category_sales)"""),
    nbf.v4.new_code_cell("""category_sales.plot(kind='bar', color=['steelblue','coral'])
plt.title('Total Sales by Category')
plt.tight_layout()
plt.savefig('../images/sales_by_category.png')
plt.show()"""),
    nbf.v4.new_code_cell("""region_sales = df.groupby('region')['total_sales'].sum().sort_values(ascending=False)
region_sales.plot(kind='bar', color='teal')
plt.title('Total Sales by Region')
plt.tight_layout()
plt.savefig('../images/sales_by_region.png')
plt.show()""")
]

with open('notebooks/sales_analysis.ipynb', 'w') as f:
    nbf.write(nb, f)

print('Notebook cree avec succes!')