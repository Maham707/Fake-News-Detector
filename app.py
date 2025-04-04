from flask import Flask, request, render_template
import pickle
import re
import nltk
from nltk.corpus import stopwords

# Initialize Flask app
app = Flask(__name__)

# Load the pre-trained model and vectorizer
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# NLTK stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Preprocessing function for the text
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\W', ' ', text)  # Remove special characters
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    words = text.split()
    words = [word for word in words if word not in stop_words]  # Remove stopwords
    return ' '.join(words)

# Home route to display the form and result
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        # Preprocess the text and vectorize it
        processed_text = preprocess_text(text)
        transformed_text = vectorizer.transform([processed_text])
        
        # Predict using the trained model
        prediction = model.predict(transformed_text)
        result = 'Fake' if prediction[0] == 0 else 'Real'
        return render_template('index.html', prediction=result)
    
    return render_template('index.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)
