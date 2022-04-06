import sys
from resource import *
import time
import psutil

GAP = 30
MISMATCH = [[0, 110, 48, 94],
            [110, 0, 118, 48],
            [48, 118, 0, 110],
            [94, 48, 110, 0]]
INDEX = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

def process_memory():
    process = psutil.Process()
    memory_info = process.memory_info()
    memory_consumed = int(memory_info.rss / 1024)
    return memory_consumed

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

def align(s1, s2):
    if s1 == s2:
        return s1, s2, 0
    if s1 == '':
        return s1, len(s1) * '_', len(s1) * GAP
    if s2 == '':
        return len(s2) * '_', s2, len(s2) * GAP
    
    s1_split = int(len(s1) / 2)
    s2_split = find_best_split_point(s1, s2)
    s1_align_left, s2_align_left, similarity_left = align(s1[:s1_split], s2[:s2_split])
    s1_align_right, s2_align_right, similarity_right = align(s1[s1_split:], s2[s2_split:])
    
    return s1_align_left + s1_align_right, s2_align_left + s2_align_right, similarity_left + similarity_right

def find_best_split_point(s1, s2):
    opt_left = [[0] * (len(s2) + 1)] * 2
    opt_left[1][0] = GAP
    for i in range(1, len(s2) + 1):
        opt_left[0][i] = GAP * i
    
    for i in range(1, int(len(s1) / 2) + 1):
        for j in range(1, len(s2) + 1):
            opt_left[1][j] = min(MISMATCH[INDEX[s1[i - 1]]][INDEX[s2[j - 1]]] + opt_left[0][j - 1], GAP + opt_left[0][j], GAP + opt_left[1][j - 1])
        
        for j in range(len(s2) + 1):
            opt_left[0][j] = opt_left[1][j]
    
    s1r = s1[::-1]
    s2r = s2[::-1]
    opt_right = [[0] * (len(s2r) + 1)] * 2
    opt_right[1][0] = GAP
    for i in range(1, len(s2r) + 1):
        opt_right[0][i] = GAP * i
    
    for i in range(1, len(s1) - int(len(s1) / 2) + 1):
        for j in range(1, len(s2r) + 1):
            opt_right[1][j] = min(MISMATCH[INDEX[s1r[i - 1]]][INDEX[s2r[j - 1]]] + opt_right[0][j - 1], GAP + opt_right[0][j], GAP + opt_right[1][j - 1])
        
        for j in range(len(s2r) + 1):
            opt_right[0][j] = opt_right[1][j]
    
    opt = 0
    opt_index = 0
    for i in range(len(s2r) + 1):
        if opt_left[1][i] + opt_right[1][len(s2r) - i] > opt:
            opt = opt_left[1][i] + opt_right[1][len(s2r) - i]
            opt_index = i
    
    return opt_index

if __name__ == "__main__":
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    s1, s2 = input_generator(input_path)
    print('s1: ', s1)
    print('s2: ', s2)
    
    start_time = time.time()
    s1_align, s2_align, similarity = align(s1, s2)
    end_time = time.time()
    time_taken = (end_time - start_time) * 1000
    
    with open(output_path, 'w') as f:
        f.writelines(str(similarity))
        f.writelines(s1_align)
        f.writelines(s2_align)
        f.writelines(time_taken)
        f.writelines(process_memory())