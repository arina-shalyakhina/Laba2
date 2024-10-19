money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
n=1
d=money_capital+salary-spend #в конце первого месяца
vv=[]
while d>0:
    n+=1
    d=d+salary-spend*(1.05**(n-1))
    if d>0:
      vv.append(d)
bbb=len(vv)+1
print("Количество месяцев, которое можно протянуть без долгов:", bbb)
