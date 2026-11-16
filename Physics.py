# PHYSICS CALCULATOR

# 1. Kinetic Energy
def kinetic_energy():
    mass = float(input("Enter mass: "))
    velocity = float(input("Enter velocity: "))

    KE = 0.5 * mass * velocity ** 2
    print("Kinetic Energy =", KE, "Joules")


# 2. Force
def force():
    mass = float(input("Enter mass: "))
    acceleration = float(input("Enter acceleration: "))

    F = mass * acceleration
    print("Force =", F, "Newtons")


# 3. Acceleration
def acceleration():
    final_velocity = float(input("Enter final velocity: "))
    initial_velocity = float(input("Enter initial velocity: "))
    time = float(input("Enter time: "))

    A = (final_velocity - initial_velocity) / time
    print("Acceleration =", A, "m/s²")


# 4. Time
def time():
    distance = float(input("Enter distance: "))
    speed = float(input("Enter speed: "))

    T = distance / speed
    print("Time =", T, "seconds")


# 5. Speed
def speed():
    distance = float(input("Enter distance: "))
    time = float(input("Enter time: "))

    S = distance / time
    print("Speed =", S, "m/s")


# MAIN PROGRAM

while True:

    print("\n===== PHYSICS CALCULATOR =====")
    print("1. Kinetic Energy")
    print("2. Force")
    print("3. Acceleration")
    print("4. Time")
    print("5. Speed")

    choice = input("Choose a physics operation (1-5): ")

    if choice == "1":
        kinetic_energy()

    elif choice == "2":
        force()

    elif choice == "3":
        acceleration()

    elif choice == "4":
        time()

    elif choice == "5":
        speed()

    else:
        print("Invalid choice. Please select 1-5.")

    continue_program = input(
        "\nWould you like to perform another calculation? (yes/no): "
    )

    if continue_program.lower() != "yes":
        print("Thank you for using the Physics Calculator!")
        break
