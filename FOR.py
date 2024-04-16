list_ = ['BMW', 'MB', 'LADA', 'KIA', 'HONDA']
cars_count = 0
for i in range(len(list_)):
    print(f'я езжу на автомобиле марки {list_[i]}')
    cars_count += 10
    print(f'cars_count = {cars_count}')
