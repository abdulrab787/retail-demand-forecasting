import matplotlib.pyplot as plt

def plot_predictions(actual, predicted, n=300):
    plt.figure(figsize=(15,6))

    plt.plot(actual.values[:n], label="Actual")
    plt.plot(predicted[:n], label="Predicted")

    plt.legend()
    plt.title("Actual vs Predicted Sales")
    plt.xlabel("Time")
    plt.ylabel("Sales")

    plt.show()
