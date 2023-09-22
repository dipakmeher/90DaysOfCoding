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


# def solution(h, q):
#     result = []

#     for label in q:
#         current = (2 ** h) - 1  # Start from the root
#         parent = (2 ** (h - 1)) - 1  # Parent of the current node

#         while current != label:
#             if current == 1 or parent == label:
#                 break
#             elif label > parent:  # If label is on the right side, move to the left
#                 current = parent - 1
#             else:  # If label is on the left side, move to the right
#                 current = parent

#             h -= 1
#             parent = (parent - 1) // 2  # Calculate the parent of the current node

#         if current == label:
#             result.append(-1)
#         else:
#             result.append(parent)

#     return result

# # Example test cases
# print(solution(3, [7, 3, 5, 1]))  # Output: [-1, 7, 6, 3]
# print(solution(5, [19, 14, 28]))   # Output: [21, 15, 29]
