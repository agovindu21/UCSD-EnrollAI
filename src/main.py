import joblib
import pandas as pd

# Load the trained model
model = joblib.load('src/open_seats_prediction_model.pkl')

# Function to predict available seats
def predict_available_seats(course, pass_num, priority, quarter_season, total=None):
    # Split department from course code (e.g., "COGS 108" → "COGS")
    department = course.split()[0]

    # If total is not provided, use a fallback average
    if total is None:
        print("Note: No total enrollment capacity provided. Using default average of 150.")
        total = 150  # You can adjust this fallback value if needed

    # Format the input data as a DataFrame
    input_data = pd.DataFrame({
        'pass': [pass_num],
        'priority': [priority],
        'total': [total],
        'department': [department],
        'course': [course],
        'quarter_season': [quarter_season]
    })

    # Predict available seats
    predicted_seats = model.predict(input_data)[0]

    # Return a non-negative number
    return max(0, predicted_seats)

# Simple command-line interface
if __name__ == '__main__':
    print("\nCourse Seat Availability Predictor")
    print("-----------------------------------")
    course = input("Enter course (e.g., COGS 108): ").strip()
    pass_num = int(input("Enter pass number (e.g., 1 or 2): "))
    priority = int(input("Enter priority level (e.g., 1 = highest): "))
    quarter_season = input("Enter quarter season (FA, WI, SP, S1, S2, S3): ").strip().upper()
    total_input = input("Enter total seat capacity (or leave blank to use default): ").strip()

    total = float(total_input) if total_input else None
    seats = predict_available_seats(course, pass_num, priority, quarter_season, total)

    print(f"\nPredicted number of available seats in {course} ({quarter_season}): {seats:.1f}")