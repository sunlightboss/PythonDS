import pandas as pd

df = pd.read_excel("/home/nursss/Загрузки/1768191995289-sales.xlsx")

print("Исходная таблица:")
print(df)

df["total_price"] = df["price"] * df["quantity"]
total_sales = df["total_price"].sum()
average_price = df["price"].mean()

print("\nОбщая сумма продаж:", total_sales)
print("Средняя цена:", average_price)

electronics_df = df[df["category"] == "Electronics"]

print("\nТовары из категории Electronics:")
print(electronics_df)

df.to_excel("sales_result.xlsx", index=False)

print("\nФайл sales_result.xlsx успешно сохранён")


########