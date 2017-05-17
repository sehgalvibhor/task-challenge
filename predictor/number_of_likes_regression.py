import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import GradientBoostingRegressor

def evaluation_predictions(true_labels, predicted_labels):
    corr = np.corrcoef(true_labels,predicted_labels)[0,1]
    mae = mean_absolute_error(true_labels, predicted_labels)
    mse = mean_squared_error(true_labels, predicted_labels)
    return corr, mae, mse


data_all = pd.read_csv('visualization.csv')
number_headers = ['statistics.commentCount','statistics.dislikeCount','statistics.viewCount','channel_commentCount','channel_subscriberCount','channel_videoCount','channel_viewCount']
text_headers = ['snippet.title','channel_description','channel_localized.description','channel_localized.title','Channel_country']
predicted_headers = ['statistics.likeCount']
sids_all = range(0,len(data_all))

number_values = []
for header in number_headers:
    number_values.append(list(data_all[header]))

text_values = []
for text in text_headers:
    text_values.append(list(data_all[text]))

actual_label = list(data_all[predicted_headers[0]])

correlation_matrix = []
for i in range(0,len(number_values)):
    value = number_values[i]
    corr = np.corrcoef(actual_label,value)
    correlation_matrix.append(corr[0,1])

##simple regression using numeric features.


##random division
train_sid, test_sid, train_labels , test_labels = train_test_split(sids_all, actual_label, test_size=0.33)

train_values = []
test_values = []
min_value = []
max_value = []
for v in number_values:
    v_train = [v[i] for i in train_sid]   
    v_test = [v[i] for i in test_sid]
    
    min_value.append(min(v_train))
    max_value.append(max(v_train))
    
    a = min(v_train)
    b = max(v_train)
    diff_ = float(b-a)
    ##normalizing features
    v_train_ = [float(v)/float(diff_) for v in v_train]
    v_test_ = [float(v)/float(diff_) for v in v_test]
    
    train_values.append(v_train_)   
    test_values.append(v_test_)


train_features = []
for i in range(0,len(train_sid)):
    train = []
    for v in train_values:
        train.append(v[i])
    train_features.append(train)

test_features = []
for i in range(0,len(test_sid)):
    test = []
    for v in test_values:
        test.append(v[i])
    test_features.append(test)


##linear_regression
##normalizing the labels and getting them to the range 0 - 100
min_label = min(train_labels)
max_label = max(train_labels)
diff_ = float(max_label) - float(min_label)

regressor = linear_model.LinearRegression(normalize=True)
regressor.fit(train_features, train_labels)

train_predictions = regressor.predict(train_features)
predictions = regressor.predict(test_features)
corr, mae, mse = evaluation_predictions(test_labels, predictions)

rms = np.sqrt(mse)
print("Correlation is ",corr)
print("Mean absolute Error is ",mae)
print("Root Mean Square is",rms)