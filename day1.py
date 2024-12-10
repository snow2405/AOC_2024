def read_input(file_path):
    with open(file_path, "r") as input_file:
        return [line.strip() for line in input_file.readlines()]

def solve_part1(data):
    total_diff = 0
    
    first_list = []
    second_list = []
    for line in data:
        parts = line.split("   ")
        first_list.append(int(parts[0])) 
        second_list.append(int(parts[1]))
    
    first_list.sort()
    second_list.sort()
    
    for i, j in zip(first_list, second_list): 
        total_diff += abs(i - j)
        
    return total_diff

def solve_part2(data):
    sim_score = 0
    
    first_list = []
    second_list = []
    for line in data:
        parts = line.split("   ")
        first_list.append(int(parts[0])) 
        second_list.append(int(parts[1]))
    
    for i in first_list: 
        count = 0
        while i in second_list: 
            count+=1
            second_list.remove(i)
        sim_score += i * count
    
    return sim_score

if __name__ == "__main__":
    print(f"Part 1: {solve_part1(read_input('input.txt'))}")
    print(f"Part 2: {solve_part2(read_input('input.txt'))}")

