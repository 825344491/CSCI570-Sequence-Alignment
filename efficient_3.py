def input_generator(path):
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
        
        for index in s1_index:
            s1 = s1[:index + 1] + s1 + s1[index + 1:]
            print(s1)
        
        for index in s2_index:
            s2 = s2[:index + 1] + s2 + s2[index + 1:]
            print(s2)
        
        return s1, s2

if __name__ == "__main__":
    s1, s2 = input_generator('SampleTestCases/input.txt')
    print('s1: ', s1)
    print('s2: ', s2)