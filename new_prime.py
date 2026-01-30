def print_primes_in_range(start, end):
    for num in range(max(2, start), end + 1):
        i = 2
        is_prime = True
        while i * i <= num:
            if num % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            print(num)

start_range = int(input("Enter the starting number: "))
end_range = int(input("Enter the ending number: "))

print(f"Prime numbers between {start_range} and {end_range} are:")
print_primes_in_range(start_range, end_range)