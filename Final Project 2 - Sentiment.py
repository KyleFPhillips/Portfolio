# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 09:40:04 2023

@author: kp503
"""

import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split

# Load the data
data = pd.read_csv('amazon.csv')

# Drop rows with NaN or null values in the 'Review' column
data.dropna(subset=['Review'], inplace=True)

# Create the tokenizer
tokenizer = Tokenizer(num_words=5000, oov_token='<OOV>')
tokenizer.fit_on_texts(data['Review'].values)

# Convert the text data to sequence
sequences = tokenizer.texts_to_sequences(data['Review'].values)
padded_sequences = pad_sequences(sequences, maxlen=100, truncating='post')

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(padded_sequences, 
                                                    data['Sentiment'].values, 
                                                    test_size=0.2, 
                                                    random_state=42)

# Define the model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(5000, 32, input_length=100),
    tf.keras.layers.LSTM(64),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', 
              metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print('Test accuracy: ', accuracy)
