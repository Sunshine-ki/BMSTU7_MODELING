from Modeller import Modeller
from prettytable import PrettyTable
from EventGenerator import Generator
from Distributions import UniformDistribution
from Processor import Processor

if __name__ == '__main__':
    table = PrettyTable()
    table.field_names = ['Количество заявок', 'обработано', 'отказано', 'процент отказа']
    clients_number = 300

    generator = Generator(
        UniformDistribution(8, 12),
        clients_number,
    )

    operators = [
        Processor(
            UniformDistribution(15, 25),
            max_queue=1,
        ),
        Processor(
            UniformDistribution(30, 50),
            max_queue=1,
        ),
        Processor(
            UniformDistribution(20, 60),
            max_queue=1,
        ),
    ]

    computers = [
        Processor(UniformDistribution(15, 15),),
        Processor(UniformDistribution(30, 30),),
    ]

    model = Modeller(generator, operators, computers)
    result = model.event_mode()
    table.add_row([clients_number, result['processed'], result['refusals'] - 1, result["refusal_percentage"]])

    print(table)

    


