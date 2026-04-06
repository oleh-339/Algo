def island_perimeter(matrix):
    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1:
                perimeter += 4

                if r > 0 and matrix[r-1][c] == 1:
                    perimeter -= 2
                    
                if c > 0 and matrix[r][c-1] == 1:
                    perimeter -= 2

    return perimeter

if __name__ == "__main__":
    test_matrix = [
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]
    ]
    
    print("Матриця островів:")
    for row in test_matrix:
        print(row)
        
    result = island_perimeter(test_matrix)
    print(f"\nЗагальна довжина берегової лінії (периметр): {result}")
