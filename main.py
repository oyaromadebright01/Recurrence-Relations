def print_recurrence_relations():
    # Recurrence relation for myfunction1
    print("Recurrence relation for myfunction1:")
    print("T(n) = T(n/2) + T(n/3) + O(n) if n > 0")
    print("T(n) = O(1) if n <= 0")
    
    # Recurrence relation for myfunction2
    print("Recurrence relation for myfunction2:")
    print("T(n) = T(n-1) + O(1) if n > 1")
    print("T(n) = O(1) if n <= 1")

# Example usage
print_recurrence_relations()
