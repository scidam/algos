import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras import backend as K
from keras.utils import plot_model
from sklearn.model_selection import train_test_split
from sklearn import datasets
iris = datasets.load_iris()


BATCH_SIZE = 15
NUM_CLASSES = 4
input_shape = 4
EPOCHS = 2000

# ------------- Building the model ----------------
model = Sequential()
model.add(Dense(20, input_shape=(input_shape,), activation='sigmoid'))
model.add(Dropout(0.1))
model.add(Dense(4, activation='sigmoid'))
model.add(Dense(10, activation='relu'))
model.add(Dense(3, activation='softmax'))
# -------------------------------------------------

# ---- Building the training and test data --------

iris = datasets.load_iris()
X = iris.data 
Y = iris.target
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.1, random_state=42, stratify=Y)

y_train = keras.utils.to_categorical(y_train, 3)
y_test = keras.utils.to_categorical(y_test, 3)
# -------------------------------------------------


# ----------- Fitting the model -------------------
model.compile(keras.optimizers.Adagrad(), loss=keras.losses.mse, metrics=['accuracy'])
model.fit(x_train, y_train,
          batch_size=BATCH_SIZE,
          epochs=EPOCHS,
          verbose=1,
          validation_split=0.4)
# -------------------------------------------------

score = model.evaluate(x_test, y_test, verbose=0)
print("Scores:", score)

print(model.predict([[0.1,0.4,0.5,0.5]]))

#plot_model(model, to_file='model.png', show_shapes=True)
