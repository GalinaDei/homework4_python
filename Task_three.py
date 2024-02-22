# 3. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
#    Дополнительно сохраняйте все операции поступления и снятия средств в список.

# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег
def main():
    balance = 0.0
    count = 0
    log_list = []
    print('Добро пожаловать в банкомат!')
    log_list.append('Авторизация')
    while True:
        while True:
            act = input('Выберите действие:\n 1 - пополнить \n 2 - снять \n 3 - посмотреть историю операций \n 4 - выйти\n')
            if act not in ("1", "2", "3", "4"):
                print("Неверный ввод")
                log_list.append('Неверный ввод')
            else:
                break
        match act:
            case "1":
                balance, count = add_money(balance, count)
                print(f"Ваш баланс {balance}")
                log_list.append('Пополнение')
            case "2":
                balance, count = get_money(balance, count)
                print(f"Ваш баланс {balance}")
                log_list.append('Снятие')
            case "3":
                print(*log_list, sep=', ')
            case "4":
                print(f"Ваш баланс {balance}")
                print("До свидания!")
                log_list.append('Выход')
                break

def add_money(balance, count):
    global summ
    if balance > 5_000_000:
        balance *= 0.9
    while True:
        try:
            summ = int(input("Введите сумму пополнения, кратную 50: "))
        except:
            ex = input("Хотите выйти в меню?\n")
            if ex.lower() == 'да':
                return balance, count
            else:
                continue
        if summ % 50 == 0:
            break
    balance += summ
    count += 1
    if count % 3 == 0:
        balance *= 1.03
    return balance, count


def get_money(balance, count):
    global summ
    if balance > 5_000_000:
        balance *= 0.9
    while True:
        try:
            summ = int(input("Введите сумму снятия, кратную 50: "))
        except:
            ex = input("Хотите выйти в меню?\n")
            if ex.lower() == 'да':
                return balance, count
            else:
                continue
        if summ % 50 == 0:
            break
    perc = summ * 0.015
    if perc < 30:
        perc = 30
    elif perc > 600:
        perc = 600
    if summ + perc > balance:
        print("Недостаточно средств!")
        pass
    else:
        balance -= (summ + perc)

    if count % 3 == 0:
        balance *= 1.03
    return balance, count


if __name__ == "__main__":
    main()
