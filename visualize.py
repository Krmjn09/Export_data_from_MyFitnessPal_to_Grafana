import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file into a Pandas DataFrame
def load_csv(file_path):
    return pd.read_csv(file_path)

# Plot data using Matplotlib
def plot_data(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df["Date"], df["Calories"], label="Calories", marker='o')
    plt.plot(df["Date"], df["Protein"], label="Protein", marker='o')
    plt.plot(df["Date"], df["Carbs"], label="Carbs", marker='o')
    plt.plot(df["Date"], df["Fat"], label="Fat", marker='o')

    plt.title("Daily Health Metrics")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.legend()
    plt.tight_layout()  # Adjust layout to prevent clipping
    plt.show()

if __name__ == "__main__":
    csv_file = "myfitnesspal_fake.csv"  # Path to your CSV file
    df = load_csv(csv_file)
    plot_data(df)