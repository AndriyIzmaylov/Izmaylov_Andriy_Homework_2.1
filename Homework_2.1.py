#Написати програму, яка просить користувача ввести 4-х значне число з клавіатури, після чого друкує
# на екрані стовпчик цифр, з якого це число складається. Наприклад, користувач вводить 1234, а програма виводить:.
#1

#2

#3

#4
#Завдання необхідно вирішити, використовуючи методи поділу (підказка // і % або divmod). Виведення в стовпчик можна
# зробити за допомогою 4-х функцій print.

#Користувач може ввести будь-яке 4 значне ціле число. Будь-яке 4-х значне число - це число, яке складається з 4-х цифр,
# де кожна цифра може бути від 0 до 9 включно.

#Ваше рішення має це враховувати! Якщо користувач ввів не ціле число, це проблема користувача, а не вашої програми.

#Створюйте рішення, виходячи з того, що число ЗАВЖДИ 4-х значне.

while True:
    try:
        entered_number = int(input("Enter a 4-digit number: "))

        if 1000 <= entered_number <= 9999:
            digit1 = entered_number // 1000
            remainder1 = abs(entered_number % 1000)
            digit2 = remainder1 // 100
            remainder2 = remainder1 % 100
            digit3 = remainder2 // 10
            digit4 = remainder2 % 10


            print(abs(digit1))
            print(digit2)
            print(digit3)
            print(digit4)
            break
        else:
            print("Error: You entered a number that is not 4 digits. Please try again.")
    except ValueError:
         print("Error: Please enter a 4-digit positive integer.")