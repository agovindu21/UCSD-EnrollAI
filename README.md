# UCSD Course Availability Predictor

A tool to predict course availability at UC San Diego, helping students plan their schedules more effectively.

## Features

- Predicts course seat availability for upcoming quarters
- Analyzes historical enrollment data
- Provides visualizations and trends
- User-friendly interface

## Getting Started

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/UCSD_Course_Availability_Predictor.git
    cd UCSD_Course_Availability_Predictor
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application:**
    ```bash
    python src/main.py
    ```

## Sample Usage

Once you have installed the dependencies and started the application, follow the prompts in the command line:

1. **Enter the course code**  
    Example: `COGS 108`

2. **Enter your pass number**  
    Options: `1` or `2`

3. **Enter your enrollment priority**  
    - `1` — Senior / Priority Enrollment  
    - `2` — Junior  
    - `3` — Sophomore  
    - `4` — Freshman  
    - `5` — Incoming Freshman

4. **Enter the quarter**  
    - `FA` — Fall  
    - `WI` — Winter  
    - `SP` — Spring  
    - `S1`, `S2` — Summer Sessions 1 and 2  
    - `S3` — Special Summer Session

5. **Enter the course capacity (optional)**  
    - Leave blank to use the historical average.

The predictor will then analyze the inputs and provide an availability prediction.

## Contributing

Contributions are welcome! Please open issues or submit pull requests.

## Disclaimer

This tool is not affiliated with UC San Diego. Predictions are based on historical data and are not guaranteed.