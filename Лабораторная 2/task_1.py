money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count_of_month = 0

while money_capital + salary - spend >= 0:
    money_capital = money_capital + salary - spend
    spend = spend + spend * increase
    count_of_month += 1
    if money_capital + salary - spend < 0:
        print("Количество месяцев, которое можно протянуть без долгов:", count_of_month)




