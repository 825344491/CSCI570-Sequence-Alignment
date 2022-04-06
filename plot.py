from cProfile import label
import matplotlib.pyplot as plt
import os

def input_size(path):
    with open(path, 'r') as f:
        s1 = f.readline().split('\n')[0]
        print(s1)
        s1_index = []
        while True:
            input = f.readline().split('\n')[0]
            if input.isdigit():
                s1_index.append(int(input))
            else:
                s2 = input
                break
        print(s1_index)
        print(s2)
        s2_index = []
        while True:
            input = f.readline().split('\n')[0]
            if input.isdigit():
                s2_index.append(int(input))
            else:
                break
        print(s2_index)
        
        m = len(s1) * pow(2, len(s1_index))
        n = len(s2) * pow(2, len(s2_index))
        return m, n

def output():
    for i in range(1, 16):
        os.system('python basic_3.py datapoints/in' + str(i) + '.txt outputs_basic/out' + str(i) + '.txt')
        os.system('python efficient_3.py datapoints/in' + str(i) + '.txt outputs_efficient/out' + str(i) + '.txt')
    # for root, ds, fs in os.walk('datapoints'):
    #     fs.sort()
    #     for f in fs:
    #         os.system('python basic_3.py ' + os.path.join(root, f) + ' outputs_basic/out' + f.split('.')[0][2:] + '.txt')
    #         os.system('python efficient_3.py ' + os.path.join(root, f) + ' outputs_efficient/out' + f.split('.')[0][2:] + '.txt')

if __name__ == "__main__":
    output()
    
    x = []
    for i in range(1, 16):
        m, n = input_size('datapoints/in' + str(i) + '.txt')
        x.append(m + n)
    # for root, ds, fs in os.walk('datapoints'):
    #     fs.sort()
    #     for f in fs:
    #         m, n = input_size(os.path.join(root, f))
    #         x.append(m + n)
    
    basic_time = []
    basic_memory = []
    for i in range(1, 16):
        with open('outputs_basic/out' + str(i) + '.txt') as f:
            for _ in range(3):
                f.readline()
            basic_time.append(float(f.readline()))
            basic_memory.append(float(f.readline()))
    # for root, ds, fs in os.walk('outputs_basic'):
    #     fs.sort()
    #     for f in fs:
    #         with open(os.path.join(root, f), 'r') as file:
    #             for _ in range(3):
    #                 file.readline()
    #             basic_time.append(float(file.readline()))
    #             basic_memory.append(float(file.readline()))
    
    efficient_time = []
    efficient_memory = []
    for i in range(1, 16):
        with open('outputs_efficient/out' + str(i) + '.txt') as f:
            for _ in range(3):
                f.readline()
            efficient_time.append(float(f.readline()))
            efficient_memory.append(float(f.readline()))
    # for root, ds, fs in os.walk('outputs_efficient'):
    #     fs.sort()
    #     for f in fs:
    #         with open(os.path.join(root, f), 'r') as file:
    #             for _ in range(3):
    #                 file.readline()
    #             efficient_time.append(float(file.readline()))
    #             efficient_memory.append(float(file.readline()))
    
    fig, ax = plt.subplots()
    ax.set_xlabel('Problem size [m+n]')
    ax.set_ylabel('CPU time [milliseconds]')
    ax.set_title('CPU time vs problem size for basic and efficient algorithm')
    ax.plot(x, basic_time, label='Basic')
    ax.plot(x, efficient_time, label='Space-efficient')
    ax.legend()
    plt.savefig('CPU time.png')
    
    fig, ax = plt.subplots()
    ax.set_xlabel('Problem size [m+n]')
    ax.set_ylabel('Memory [KB]')
    ax.set_title('Memory usage vs problem size for basic and efficient algorithm')
    ax.plot(x, basic_memory, label='Basic')
    ax.plot(x, efficient_memory, label='Space-efficient')
    ax.legend()
    plt.savefig('Memory.png')