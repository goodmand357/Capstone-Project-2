import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# --- Step 1: Create dummy stock data ---
def generate_dummy_data(n=200):
    np.random.seed(42)
    df = pd.DataFrame({
        "price_momentum": np.random.randn(n),
        "rsi": np.random.uniform(10, 90, n),
        "macd": np.random.randn(n),
        "volume_change": np.random.randn(n),
        "target": np.random.randint(0, 2, n)  # 1 = Up, 0 = Down
    })
    return df

# --- Step 2: Train the ML model ---
def train_model():
    df = generate_dummy_data()
    X = df.drop("target", axis=1)
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    return model, acc

# Train once at load time (optional)
model, accuracy = train_model()

# --- Step 3: Predict a stock's direction ---
def predict_stock(features):
    """
    features: dict with keys - price_momentum, rsi, macd, volume_change
    """
    X_input = pd.DataFrame([features])
    prediction = model.predict(X_input)[0]
    label = "Up" if prediction == 1 else "Down"
    return {"prediction": label, "accuracy": round(accuracy * 100, 2)}
