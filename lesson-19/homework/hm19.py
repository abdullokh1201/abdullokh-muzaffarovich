import pandas as pd

# Загрузка данных из CSV файла
df = pd.read_csv('task/sales_data.csv')

# Агрегированные статистики по категориям
agg_stats = df.groupby('Category').agg(
    Total_Quantity_Sold=('Quantity', 'sum'),
    Average_Price_per_Unit=('Price', 'mean'),
    Max_Quantity_Sold=('Quantity', 'max')
).reset_index()

print("Агрегированные статистики по категориям:")
print(agg_stats)
print()

# Топ-продукт в каждой категории по общему количеству проданных единиц
top_products = (
    df.groupby(['Category', 'Product'])['Quantity']
      .sum()
      .reset_index()
      .sort_values(['Category', 'Quantity'], ascending=[True, False])
      .groupby('Category')
      .first()
      .reset_index()
      .rename(columns={'Product': 'Top_Selling_Product', 'Quantity': 'Total_Quantity_Sold'})
)

print("Топ-продукты по категориям:")
print(top_products)
print()

#  Дата с максимальными общими продажами (Quantity * Price)
df['Total_Sales'] = df['Quantity'] * df['Price']
sales_by_date = df.groupby('Date')['Total_Sales'].sum().reset_index()
max_sales_date = sales_by_date.loc[sales_by_date['Total_Sales'].idxmax()]

print("Дата с максимальными продажами:")
print(max_sales_date)

#2.

import pandas as pd

# Загрузим данные из CSV
df = pd.read_csv('task/customer_orders.csv', sep='\t')

#  Группируем по CustomerID и фильтруем клиентов с количеством заказов >= 20
orders_count = df.groupby('CustomerID').size()
customers_20plus = orders_count[orders_count >= 20].index
df_20plus = df[df['CustomerID'].isin(customers_20plus)]

print("Клиенты с количеством заказов >= 20:")
print(customers_20plus.tolist())
print()

#  Находим клиентов с средней ценой за продукт > 120
avg_price_per_customer = df.groupby('CustomerID')['Price'].mean()
customers_avg_price_gt_120 = avg_price_per_customer[avg_price_per_customer > 120].index
print("Клиенты со средней ценой продукта > $120:")
print(customers_avg_price_gt_120.tolist())
print()

#  Для каждого продукта считаем суммарное количество и общую стоимость (Quantity * Price)
product_totals = df.groupby('Product').agg(
    Total_Quantity=('Quantity', 'sum'),
    Total_Price=('Price', lambda x: (df.loc[x.index, 'Quantity'] * x).sum())
).reset_index()

# Фильтруем продукты с суммарным количеством >= 5
products_filtered = product_totals[product_totals['Total_Quantity'] >= 5]

print("Продукты с суммарным количеством >= 5:")
print(products_filtered)

#3.

import sqlite3
import pandas as pd
import numpy as np

# 1. Считываем данные из SQLite
conn = sqlite3.connect('task/population.db')
query = "SELECT * FROM population"
df = pd.read_sql_query(query, conn)
conn.close()

# 2. Считываем Salary Band из Excel
salary_bands_df = pd.read_excel('task/population salary analysis.xlsx')

# Пример, как может выглядеть salary_bands_df (нужно адаптировать под ваш файл):
# | Salary Band               | Percentage | Average Salary | Median Salary | Number of population |
# |--------------------------|------------|----------------|---------------|----------------------|
# | till $200,000            |            |                |               |                      |
# | $200,001 - $400,000      |            |                |               |                      |
# | ...                      |            |                |               |                      |

# Для удобства создадим в Python список кортежей с интервалами зарплат из колонки 'Salary Band'

def parse_band(band):
    # Пример парсинга строкового диапазона зарплаты
    band = band.strip()
    if 'till' in band:
        upper = int(band.split('$')[1].replace(',', '').replace('.', ''))
        return (0, upper)
    elif 'and over' in band:
        lower = int(band.split('$')[1].replace(',', '').replace('.', ''))
        return (lower, np.inf)
    else:
        parts = band.replace('$', '').replace(',', '').split('-')
        lower = int(parts[0])
        upper = int(parts[1])
        return (lower, upper)

salary_ranges = [parse_band(band) for band in salary_bands_df['Salary Band']]

# 3. Создаем функцию для присвоения категории зарплаты каждому человеку

def assign_salary_band(salary):
    for i, (low, high) in enumerate(salary_ranges):
        if low <= salary <= high:
            return salary_bands_df['Salary Band'][i]
    return None

df['Salary Band'] = df['Salary'].apply(assign_salary_band)

# 4. Расчеты по всей популяции

total_population = len(df)

summary = []

for band in salary_bands_df['Salary Band']:
    band_df = df[df['Salary Band'] == band]
    count = len(band_df)
    if count == 0:
        avg_salary = np.nan
        median_salary = np.nan
        perc = 0
    else:
        avg_salary = band_df['Salary'].mean()
        median_salary = band_df['Salary'].median()
        perc = (count / total_population) * 100
    summary.append({
        'Salary Band': band,
        'Percentage': perc,
        'Average Salary': avg_salary,
        'Median Salary': median_salary,
        'Number of population': count
    })

summary_df = pd.DataFrame(summary)

print("Summary по всей популяции:")
print(summary_df)

# 5. Аналогично считаем по каждому штату

states = df['State'].unique()

state_summaries = []

for state in states:
    state_df = df[df['State'] == state]
    total_pop_state = len(state_df)
    for band in salary_bands_df['Salary Band']:
        band_df = state_df[state_df['Salary Band'] == band]
        count = len(band_df)
        if count == 0:
            avg_salary = np.nan
            median_salary = np.nan
            perc = 0
        else:
            avg_salary = band_df['Salary'].mean()
            median_salary = band_df['Salary'].median()
            perc = (count / total_pop_state) * 100
        state_summaries.append({
            'State': state,
            'Salary Band': band,
            'Percentage': perc,
            'Average Salary': avg_salary,
            'Median Salary': median_salary,
            'Number of population': count
        })

state_summary_df = pd.DataFrame(state_summaries)

print("\nSummary по штатам:")
print(state_summary_df)


