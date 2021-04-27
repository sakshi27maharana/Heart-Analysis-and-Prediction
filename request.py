import requests
data = {
    'thall_fixed defect': 1,
    'thall_reversable defect': 0,
    'thall_normal': 1,
    'restecg_normal': 1,
    'restecg_left ventricular hypertrophy': 0,
    'cp_typical angina': 1,
    'cp_non-anginal pain': 1,
    'cp_atypical angina': 0,
    'caa': 0,
    'slp': 1
  }

url = "http://localhost:5005/predict_api"
response = requests.post(url, json=data)
print("Churn: " + str(response.json()))
