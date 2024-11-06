from datetime import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == "__main__":

    start = datetime.now()
    for file_name in filenames:
        read_info(file_name)
    end = datetime.now()
    print(filenames)
    print(f'{end - start} (Линейный)')

    start1 = datetime.now()
    with Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    print(filenames)
    end1 = datetime.now()
    print(f'{end1 - start1} (Многопроцессный)')
