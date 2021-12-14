from event_model import event_model
from step_model import step_model

from distributions import EvenDistribution, NormalDistribution


def main():
    a, b = 1, 10
    generator = EvenDistribution(a, b)

    mu, sigma = 5, 0.3
    processor = NormalDistribution(mu, sigma)

    total_tasks = 1000
    repeat_percentage = 100
    step = 0.01

    print("Максимальная длина очереди:")
    print('Event model:', event_model(generator, processor, total_tasks, repeat_percentage))
    print('Step model:', step_model(generator, processor, total_tasks, repeat_percentage, step))


if __name__ == '__main__':
    main()
