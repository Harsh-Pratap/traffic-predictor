import sys
import joblib
import numpy as np

# Load scalers and model
x_scaler = joblib.load('model/x_scaler.pkl')
y_scaler = joblib.load('model/y_scaler.pkl')
model = joblib.load('model/traffic_model.pkl')

# Get input data from command line arguments
input_data = [float(x) for x in sys.argv[1:]]
input_data = np.array([input_data])

# Scale input data using x_scaler
input_scaled = x_scaler.transform(input_data)

# Predict the result using the model
pred_scaled = model.predict(input_scaled).reshape(-1, 1)

# Inverse scale the prediction using y_scaler
pred_actual = y_scaler.inverse_transform(pred_scaled)

# Print the actual predicted value
print("Prediction:", pred_actual[0][0])
