
def status_lulus(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


# Test case
print("Test 1:", status_lulus(75))
print("Test 2:", status_lulus(60))
print("Test 3:", status_lulus(59))
print("Test 4:", status_lulus(0))
print("Test 5:", status_lulus(100))
