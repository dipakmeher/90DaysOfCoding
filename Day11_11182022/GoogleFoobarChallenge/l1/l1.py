# Need to revise
def calculate_square_tiles(area):
    square_sizes = []
    while area > 0:
        largest_square = int(area * 0.5) * 2
        square_sizes.append(largest_square)
        area -= largest_square
    return square_sizes

# Example usage:
area = 12
tiles = calculate_square_tiles(area)
print(tiles)  # Output: [9, 1, 1, 1]