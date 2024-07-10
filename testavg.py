import matplotlib.pyplot as plt

li = []

def create_list():
    num = int(input("How many numbers do you need in the list? "))
    for _ in range(num):
        i = int(input("Put in your number: "))
        li.append(i)
    print("List of numbers:", li)

def movavg():
    unit = int(input("How many units are we using for the moving average? "))
    
    if unit < 1:
        print("Window size must be at least 1.")
        return

    averages = []
    for i in range(len(li)):
        if i < unit - 1:
            # Not enough elements for the full window, use partial window
            window = li[:i + 1]
        else:
            # Full window
            window = li[i - unit + 1:i + 1]
        averages.append(sum(window) / len(window))

    print("Moving Averages:", averages)
    
    # Plotting the data and moving average
    plt.figure(figsize=(10, 6))
    plt.plot(li, label='Original Data')
    plt.plot(averages, label='Moving Average', linestyle='--')
    plt.title('Moving Average with Window Size {}'.format(unit))
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.legend()
    plt.show()

# Create the list
create_list()

# Calculate and plot the moving average
movavg()
