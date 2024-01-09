# Turbofan-RUL-Prediction

## Overview
This project focuses on developing predictive models for estimating the Remaining Useful Life (RUL) of aircraft turbofan engines. Utilizing advanced machine learning techniques, the project aims to analyze time series data from aircraft engine simulations and predict the time until maintenance is required.

## Dataset
The dataset used in this project is derived from the "Turbofan Engine Degradation Simulation Data Set 2," provided by NASA's Prognostics Center of Excellence. It includes simulated degradation paths under various operational conditions and fault scenarios for a fleet of turbofan engines.

- **Data Source**: [NASA Prognostics Data Repository](https://phm-datasets.s3.amazonaws.com/NASA/17.+Turbofan+Engine+Degradation+Simulation+Data+Set+2.zip)
- **Citation**: M. Chao, C. Kulkarni, K. Goebel, and O. Fink (2021). "Aircraft Engine Run-to-Failure Dataset under real flight conditions."

## Project Structure
- `data/`: Contains the dataset files.
- `notebooks/`: Jupyter notebooks for data preprocessing, analysis, and model development.
- `src/`: Source code for the project.
- `requirements.txt`: List of dependencies for the project.

## Getting Started
1. **Clone the Repository**: 
   ```
   git clone https://github.com/Iraj-Ahangari/Turbofan-RUL-Prediction.git
   ```
2. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```
3. **Explore the Notebooks**:
   Navigate to the `notebooks/` directory and run Jupyter notebooks.

## Models and Techniques
- Exploratory Data Analysis (EDA) for understanding the dataset characteristics.
- Feature Engineering to extract meaningful information from time series data.
- Implementation of machine learning models like RNN, LSTM, and others for RUL prediction.

## Contribution
Contributions to this project are welcome. Feel free to fork the repo, make improvements, and submit pull requests.

## License
This project is licensed under the terms of the MIT license.

## Contact
For inquiries or suggestions, please contact ahangarii@gmail.com .

