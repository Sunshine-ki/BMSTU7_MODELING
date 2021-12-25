from Modeller import Modeller
from prettytable import PrettyTable
from EventGenerator import Generator
from Distributions import UniformDistribution
from Processor import Processor

if __name__ == '__main__':
    # Количество клиентов
    clients_number = 300 

    # Время обслуживания оператора
    operator_time = 2 
    # Погрешность обслуживания оператора
    operator_delta = 1 

    # Время обслуживания машины
    computer_time = 1 
    # Погрешность обслуживания машины
    computer_delta = 1 

    # Время прихода клиента
    clients_time = 1 
    # Погрешность времени прихода клиента
    clients_delta = 1 

    generator = Generator(
        UniformDistribution(0, 2),
        clients_number,
    )

    operators = [
        Processor(UniformDistribution(operator_time - operator_delta, operator_delta + operator_time)),
        Processor(UniformDistribution(operator_time - operator_delta, operator_delta + operator_time)),
        Processor(UniformDistribution(operator_time - operator_delta, operator_delta + operator_time)),
    ]

    computers = [
        Processor(UniformDistribution(computer_time - computer_delta, computer_delta + computer_time),),
        Processor(UniformDistribution(computer_time - computer_delta, computer_delta + computer_time),),
        Processor(UniformDistribution(computer_time - computer_delta, computer_delta + computer_time),),
    ]

    generator.receivers = operators.copy()
    operators[0].receivers = computers
    operators[1].receivers = computers
    operators[2].receivers = computers

    model = Modeller(generator, operators, computers)
    result = model.event_mode()

    table2 = PrettyTable()
    table2.add_column('Элементы', [('Оператор '+ str(i + 1)) for i in range(len(operators))] + [('Машина ' + str(i + 1)) for i in range(len(computers))])
    table2.add_column('Максимальная очередь', result['max_queue'])
    table2.add_column('Обработано', result['proc_arr'])
    
    print("Количество заявок: ", clients_number)
    print("Время работы: " + str(result['time']))
    print(table2)

    


