import math

print("==============================================")
print(" WIRELESS POWER TRANSFER COIL OPTIMIZATION")
print("==============================================")

L1 = float(input("Enter transmitter coil inductance (uH): "))
L2 = float(input("Enter receiver coil inductance (uH): "))
Q1 = float(input("Enter transmitter quality factor Q1: "))
Q2 = float(input("Enter receiver quality factor Q2: "))

L1_H = L1 * 1e-6
L2_H = L2 * 1e-6

best_efficiency = 0
best_k = 0
best_mutual_inductance = 0

print("\nOptimization Results")
print("--------------------")

for k in [i / 100 for i in range(1, 101)]:

    mutual_inductance = k * math.sqrt(L1_H * L2_H)

    efficiency = (
        (k ** 2 * Q1 * Q2)
        / (1 + k ** 2 * Q1 * Q2)
    ) * 100

    print(
        f"k = {k:.2f} | "
        f"M = {mutual_inductance * 1e6:.3f} uH | "
        f"Efficiency = {efficiency:.2f}%"
    )

    if efficiency > best_efficiency:
        best_efficiency = efficiency
        best_k = k
        best_mutual_inductance = mutual_inductance

print("\n==============================================")
print(" OPTIMIZED COIL PARAMETERS")
print("==============================================")

print(f"Best Coupling Coefficient: {best_k:.2f}")
print(
    f"Mutual Inductance: "
    f"{best_mutual_inductance * 1e6:.3f} uH"
)
print(f"Maximum Estimated Efficiency: {best_efficiency:.2f}%")

if best_efficiency >= 80:
    print("Status: HIGH TRANSFER EFFICIENCY")
elif best_efficiency >= 50:
    print("Status: MODERATE TRANSFER EFFICIENCY")
else:
    print("Status: LOW TRANSFER EFFICIENCY")

print("\nNote: This is a simplified educational model.")
