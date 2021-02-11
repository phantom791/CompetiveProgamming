def solve(values, size):
    solution = [None] * size

    def extend_solution(position):
        for value in values:
            solution[position] = value
            print(solution)
            if no_adjacencies(solution, position):
                if position >= size-1 or extend_solution(position+1):
                    return solution
        return None

    return extend_solution(0)

def no_adjacencies(string, up_to_index):
    length = up_to_index+1
    for j in range(1, length//2+1):
        if (string[length-2*j:length-j] == string[length-j:length]):
            return False
    return True

print(''.join(str(v) for v in solve(range(3), 50)))