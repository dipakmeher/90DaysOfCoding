def solution(h, q):
    def find_parent(label):
        if label == (1 << h) - 1:  # Root node, no parent
            return -1
        
        parent = (1 << h) - 1  # Start at the root node
        depth = h
        
        while depth > 1:
            left_child = parent - (1 << (depth - 1))
            right_child = parent - 1
            
            if label == left_child or label == right_child:
                return parent
            
            if label < left_child:
                parent = left_child
            else:
                parent = right_child
            
            depth -= 1
        
        return -1

    return [find_parent(label) for label in q]

# Example test cases
print(solution(3, [7, 3, 5, 1]))  # Output: [-1, 7, 6, 3]
print(solution(5, [19, 14, 28]))   # Output: [21, 15, 29]
