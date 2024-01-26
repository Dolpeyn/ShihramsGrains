def grains():
    total_grains = 0
    grains_on_current_square = 1

    for square in range(1, 65):  # There are 64 squares on a chessboard
        total_grains += grains_on_current_square
        print(f"Square: {square}, Grains: {grains_on_current_square}")
        grains_on_current_square *= 2
    print(f"Square: {square}, Grains: {grains_on_current_square}")
    return total_grains

result = grains()
print(f"\nThe Grand Vizier requested a total of {result} grains.")