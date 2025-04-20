import pandas as pd
from sklearn.calibration import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
import pickle
import os

def load_and_preprocess_data():
    """Загрузка и предобработка данных"""
    df = pd.read_csv('Titanic.csv', delimiter=',')
    df = df.dropna()
    
    # Кодирование категориальных признаков
    categories = df.select_dtypes(include=('object')).columns
    for col in categories:
        df[col] = LabelEncoder().fit_transform(df[col])
    
    return df

def train_model(X_train, y_train):
    """Обучение модели"""
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=5,
        random_state=42
    )
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """Оценка модели"""
    y_pred = model.predict(X_test)
    return {
        'accuracy': accuracy_score(y_test, y_pred),
        'f1': f1_score(y_test, y_pred),
        'roc_auc': roc_auc_score(y_test, y_pred)
    }

def save_model(model, filename='model.pkl'):
    """Сохранение модели в файл"""
    with open(filename, 'wb') as f:
        pickle.dump(model, f)
    print(f"Model saved as {filename}")

def main():
    # 1. Загрузка и подготовка данных
    df = load_and_preprocess_data()
    
    # 2. Разделение на признаки и целевую переменную
    X = df.drop('Survived', axis=1)
    y = df['Survived']
    
    # 3. Разделение на train/test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 4. Обучение модели
    model = train_model(X_train, y_train)
    
    # 5. Оценка модели
    metrics = evaluate_model(model, X_test, y_test)
    print("Model metrics:")
    print(f"Accuracy: {metrics['accuracy']:.4f}")
    print(f"F1 Score: {metrics['f1']:.4f}")
    print(f"ROC AUC: {metrics['roc_auc']:.4f}")
    
    # 6. Сохранение модели
    save_model(model)
    
    # 7. Сохранение метрик в файл для Jenkins
    with open('metrics.txt', 'w') as f:
        f.write(f"Accuracy: {metrics['accuracy']:.4f}\n")
        f.write(f"F1 Score: {metrics['f1']:.4f}\n")
        f.write(f"ROC AUC: {metrics['roc_auc']:.4f}\n")

if __name__ == "__main__":
    main()