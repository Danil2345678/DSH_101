salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0  # Подушка безопасности

for i in range(months):
    dificit_of_month = spend - salary      # Ежемесячный дефицит
    spend = spend + spend * increase
    money_capital = money_capital + dificit_of_month
    if i == months - 1:
        money_capital = round(money_capital)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
