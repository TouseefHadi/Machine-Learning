import streamlit as st
import pickle
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import string

nltk.download('punkt')
nltk.download('stopwords')

# Create a stemming object
ps = PorterStemmer()

# Function to transform the text
def updated_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


tfidf = pickle.load(open('vectorizer_file.pkl','rb'))
model = pickle.load(open('model_file.pkl','rb'))

st.title("Classify your email as spam or not-spam")

input_sms = st.text_area("Enter the email or message here")

if st.button('click-predict'):

    # 1. preprocess
    transformed_sms = updated_text(input_sms)
    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 1:
        st.header("Yes, it's Spam")
    else:
        st.header("No, its not Spam")
