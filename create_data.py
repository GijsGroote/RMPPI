import numpy as np


def main():
    # with open('data_path/data.txt', 'w') as data:
    data_array = np.random.random((1000, 1000))
    print(data_array.shape)
    np.save('weigths_path/60_steps', data_array)


if __name__ == '__main__':
    main()
