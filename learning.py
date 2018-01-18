# for handling the data
import pandas as pd
# for matrix computations
import numpy as np

# for plotting
import seaborn as sns
# %matplotlib inline

from sklearn import datasets

# the different algorithms
from sklearn.ensemble import RandomForestClassifier as rf
from sklearn.tree import DecisionTreeClassifier as dtc
from sklearn.svm import SVC as svc
from sklearn.linear_model import LogisticRegression as lr
from sklearn.ensemble import AdaBoostClassifier


# for learning and the evaluation
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import GridSearchCV

from sklearn.preprocessing import MinMaxScaler

# slice dictionary
from itertools import islice
import json, heapq

# mapping list
# country2continent = {'EH': 'OTHER', 'PN': 'OTHER', 'TF': 'OTHER', 'JE': 'EU', 'TP': 'AS', 'YU': 'EU', 'BL': 'NA', 'AX': 'EU', 'HM': 'OTHER', 'GS': 'OTHER', 'AN': 'OTHER', 'DZ': 'OTHER', 'AO': 'OTHER', 'SH': 'OTHER', 'BJ': 'OTHER', 'BW': 'OTHER', 'BF': 'OTHER', 'BI': 'OTHER', 'CM': 'OTHER', 'CV': 'OTHER', 'CF': 'OTHER', 'TD': 'OTHER', 'KM': 'OTHER', 'CG': 'OTHER', 'CD': 'OTHER', 'DJ': 'OTHER', 'EG': 'OTHER', 'GQ': 'OTHER', 'ER': 'OTHER', 'ET': 'OTHER', 'GA': 'OTHER', 'GM': 'OTHER', 'GH': 'OTHER', 'GN': 'OTHER', 'GW': 'OTHER', 'CI': 'OTHER', 'KE': 'OTHER', 'LS': 'OTHER', 'LR': 'OTHER', 'LY': 'OTHER', 'MG': 'OTHER', 'MW': 'OTHER', 'ML': 'OTHER', 'MR': 'OTHER', 'MU': 'OTHER', 'YT': 'OTHER', 'MA': 'OTHER', 'MZ': 'OTHER', 'NA': 'OTHER', 'NE': 'OTHER', 'NG': 'OTHER', 'ST': 'OTHER', 'RE': 'OTHER', 'RW': 'OTHER', 'SN': 'OTHER', 'SC': 'OTHER', 'SL': 'OTHER', 'SO': 'OTHER', 'ZA': 'OTHER', 'SS': 'OTHER', 'SD': 'OTHER', 'SZ': 'OTHER', 'TZ': 'OTHER', 'TG': 'OTHER', 'TN': 'OTHER', 'UG': 'OTHER', 'ZM': 'OTHER', 'ZW': 'OTHER', 'AQ': 'OTHER', 'AF': 'AS', 'AM': 'AS', 'AZ': 'AS', 'BH': 'AS', 'BD': 'AS', 'BT': 'AS', 'BN': 'AS', 'KH': 'AS', 'CN': 'AS', 'CX': 'AS', 'CC': 'AS', 'IO': 'AS', 'GE': 'AS', 'HK': 'AS', 'IN': 'AS', 'ID': 'AS', 'IR': 'AS', 'IQ': 'AS', 'IL': 'AS', 'JP': 'AS', 'JO': 'AS', 'KZ': 'AS', 'KW': 'AS', 'KG': 'AS', 'LA': 'AS', 'LB': 'AS', 'MO': 'AS', 'MY': 'AS', 'MV': 'AS', 'MN': 'AS', 'MM': 'AS', 'NP': 'AS', 'KP': 'AS', 'OM': 'AS', 'PK': 'AS', 'PS': 'AS', 'PH': 'AS', 'QA': 'AS', 'SA': 'AS', 'SG': 'AS', 'KR': 'AS', 'LK': 'AS', 'SY': 'AS', 'TW': 'AS', 'TJ': 'AS', 'TH': 'AS', 'TR': 'AS', 'TM': 'AS', 'AE': 'AS', 'UZ': 'AS', 'VN': 'AS', 'YE': 'AS', 'AS': 'OTHER', 'AU': 'OTHER', 'NZ': 'OTHER', 'CK': 'OTHER', 'TL': 'OTHER', 'FM': 'OTHER', 'FJ': 'OTHER', 'PF': 'OTHER', 'GU': 'OTHER', 'KI': 'OTHER', 'MP': 'OTHER', 'MH': 'OTHER', 'UM': 'OTHER', 'NR': 'OTHER', 'NC': 'OTHER', 'NU': 'OTHER', 'NF': 'OTHER', 'PW': 'OTHER', 'PG': 'OTHER', 'WS': 'OTHER', 'SB': 'OTHER', 'TK': 'OTHER', 'TO': 'OTHER', 'TV': 'OTHER', 'VU': 'OTHER', 'WF': 'OTHER', 'AL': 'EU', 'AD': 'EU', 'AT': 'EU', 'BY': 'EU', 'BE': 'EU', 'BA': 'EU', 'BG': 'EU', 'HR': 'EU', 'CY': 'EU', 'CZ': 'EU', 'DK': 'EU', 'EE': 'EU', 'FO': 'EU', 'FI': 'EU', 'FR': 'EU', 'DE': 'EU', 'GI': 'EU', 'GR': 'EU', 'HU': 'EU', 'IS': 'EU', 'IE': 'EU', 'IM': 'EU', 'IT': 'EU', 'XK': 'EU', 'LV': 'EU', 'LI': 'EU', 'LT': 'EU', 'LU': 'EU', 'MK': 'EU', 'MT': 'EU', 'MD': 'EU', 'MC': 'EU', 'ME': 'EU', 'NL': 'EU', 'NO': 'EU', 'PL': 'EU', 'PT': 'EU', 'RO': 'EU', 'RU': 'EU', 'SM': 'EU', 'RS': 'EU', 'SK': 'EU', 'SI': 'EU', 'ES': 'EU', 'SE': 'EU', 'CH': 'EU', 'UA': 'EU', 'GB': 'EU', 'VA': 'EU', 'FX': 'EU', 'SJ': 'EU', 'AI': 'NA', 'AG': 'NA', 'AW': 'NA', 'BS': 'NA', 'BB': 'NA', 'BZ': 'NA', 'BM': 'NA', 'BQ': 'NA', 'VG': 'NA', 'CA': 'NA', 'KY': 'NA', 'CR': 'NA', 'CU': 'NA', 'CW': 'NA', 'DM': 'NA', 'DO': 'NA', 'SV': 'NA', 'GL': 'NA', 'GD': 'NA', 'GP': 'NA', 'GT': 'NA', 'HT': 'NA', 'HN': 'NA', 'JM': 'NA', 'MQ': 'NA', 'MX': 'NA', 'PM': 'NA', 'MS': 'NA', 'KN': 'NA', 'NI': 'NA', 'PA': 'NA', 'PR': 'NA', 'SX': 'NA', 'LC': 'NA', 'VC': 'NA', 'TT': 'NA', 'TC': 'NA', 'US': 'NA', 'VI': 'NA', 'AR': 'OTHER', 'BO': 'OTHER', 'BR': 'OTHER', 'CL': 'OTHER', 'CO': 'OTHER', 'EC': 'OTHER', 'FK': 'OTHER', 'GF': 'OTHER', 'GY': 'OTHER', 'PY': 'OTHER', 'PE': 'OTHER', 'SR': 'OTHER', 'UY': 'OTHER', 'VE': 'OTHER'}
country2continent = {'EH': 'OTHER', 'PN': 'OTHER', 'TF': 'OTHER', 'JE': 'EU', 'TP': 'AS', 'YU': 'EU', 'BL': 'NA', 'AX': 'EU', 'HM': 'OTHER', 'GS': 'OTHER', 'AN': 'OTHER', 'DZ': 'OTHER', 'AO': 'OTHER', 'SH': 'OTHER', 'BJ': 'OTHER', 'BW': 'OTHER', 'BF': 'OTHER', 'BI': 'OTHER', 'CM': 'OTHER', 'CV': 'OTHER', 'CF': 'OTHER', 'TD': 'OTHER', 'KM': 'OTHER', 'CG': 'OTHER', 'CD': 'OTHER', 'DJ': 'OTHER', 'EG': 'OTHER', 'GQ': 'OTHER', 'ER': 'OTHER', 'ET': 'OTHER', 'GA': 'OTHER', 'GM': 'OTHER', 'GH': 'OTHER', 'GN': 'OTHER', 'GW': 'OTHER', 'CI': 'OTHER', 'KE': 'OTHER', 'LS': 'OTHER', 'LR': 'OTHER', 'LY': 'OTHER', 'MG': 'OTHER', 'MW': 'OTHER', 'ML': 'OTHER', 'MR': 'OTHER', 'MU': 'OTHER', 'YT': 'OTHER', 'MA': 'OTHER', 'MZ': 'OTHER', 'NA': 'OTHER', 'NE': 'OTHER', 'NG': 'OTHER', 'ST': 'OTHER', 'RE': 'OTHER', 'RW': 'OTHER', 'SN': 'OTHER', 'SC': 'OTHER', 'SL': 'OTHER', 'SO': 'OTHER', 'ZA': 'OTHER', 'SS': 'OTHER', 'SD': 'OTHER', 'SZ': 'OTHER', 'TZ': 'OTHER', 'TG': 'OTHER', 'TN': 'OTHER', 'UG': 'OTHER', 'ZM': 'OTHER', 'ZW': 'OTHER', 'AQ': 'OTHER', 'AF': 'AS', 'AM': 'AS', 'AZ': 'AS', 'BH': 'AS', 'BD': 'AS', 'BT': 'AS', 'BN': 'AS', 'KH': 'AS', 'CN': 'AS', 'CX': 'AS', 'CC': 'AS', 'IO': 'AS', 'GE': 'AS', 'HK': 'AS', 'IN': 'AS', 'ID': 'AS', 'IR': 'AS', 'IQ': 'AS', 'IL': 'AS', 'JP': 'AS', 'JO': 'AS', 'KZ': 'AS', 'KW': 'AS', 'KG': 'AS', 'LA': 'AS', 'LB': 'AS', 'MO': 'AS', 'MY': 'AS', 'MV': 'AS', 'MN': 'AS', 'MM': 'AS', 'NP': 'AS', 'KP': 'AS', 'OM': 'AS', 'PK': 'AS', 'PS': 'AS', 'PH': 'AS', 'QA': 'AS', 'SA': 'AS', 'SG': 'AS', 'KR': 'AS', 'LK': 'AS', 'SY': 'AS', 'TW': 'AS', 'TJ': 'AS', 'TH': 'AS', 'TR': 'AS', 'TM': 'AS', 'AE': 'AS', 'UZ': 'AS', 'VN': 'AS', 'YE': 'AS', 'AS': 'OTHER', 'AU': 'OTHER', 'NZ': 'OTHER', 'CK': 'OTHER', 'TL': 'OTHER', 'FM': 'OTHER', 'FJ': 'OTHER', 'PF': 'OTHER', 'GU': 'OTHER', 'KI': 'OTHER', 'MP': 'OTHER', 'MH': 'OTHER', 'UM': 'OTHER', 'NR': 'OTHER', 'NC': 'OTHER', 'NU': 'OTHER', 'NF': 'OTHER', 'PW': 'OTHER', 'PG': 'OTHER', 'WS': 'OTHER', 'SB': 'OTHER', 'TK': 'OTHER', 'TO': 'OTHER', 'TV': 'OTHER', 'VU': 'OTHER', 'WF': 'OTHER', 'AL': 'EU', 'AD': 'EU', 'AT': 'EU', 'BY': 'EU', 'BE': 'EU', 'BA': 'EU', 'BG': 'EU', 'HR': 'EU', 'CY': 'EU', 'CZ': 'EU', 'DK': 'EU', 'EE': 'EU', 'FO': 'EU', 'FI': 'EU', 'FR': 'EU', 'DE': 'EU', 'GI': 'EU', 'GR': 'EU', 'HU': 'EU', 'IS': 'EU', 'IE': 'EU', 'IM': 'EU', 'IT': 'EU', 'XK': 'EU', 'LV': 'EU', 'LI': 'EU', 'LT': 'EU', 'LU': 'EU', 'MK': 'EU', 'MT': 'EU', 'MD': 'EU', 'MC': 'EU', 'ME': 'EU', 'NL': 'EU', 'NO': 'EU', 'PL': 'EU', 'PT': 'EU', 'RO': 'EU', 'RU': 'EU', 'SM': 'EU', 'RS': 'EU', 'SK': 'EU', 'SI': 'EU', 'ES': 'EU', 'SE': 'EU', 'CH': 'EU', 'UA': 'EU', 'GB': 'EU', 'VA': 'EU', 'FX': 'EU', 'SJ': 'EU', 'AI': 'NA', 'AG': 'NA', 'AW': 'NA', 'BS': 'NA', 'BB': 'NA', 'BZ': 'NA', 'BM': 'NA', 'BQ': 'NA', 'VG': 'NA', 'CA': 'NA', 'KY': 'NA', 'CR': 'NA', 'CU': 'NA', 'CW': 'NA', 'DM': 'NA', 'DO': 'NA', 'SV': 'NA', 'GL': 'NA', 'GD': 'NA', 'GP': 'NA', 'GT': 'NA', 'HT': 'NA', 'HN': 'NA', 'JM': 'NA', 'MQ': 'NA', 'MX': 'NA', 'PM': 'NA', 'MS': 'NA', 'KN': 'NA', 'NI': 'NA', 'PA': 'NA', 'PR': 'NA', 'SX': 'NA', 'LC': 'NA', 'VC': 'NA', 'TT': 'NA', 'TC': 'NA', 'US': 'NA', 'VI': 'NA', 'AR': 'OTHER', 'BO': 'OTHER', 'BR': 'OTHER', 'CL': 'OTHER', 'CO': 'OTHER', 'EC': 'OTHER', 'FK': 'OTHER', 'GF': 'OTHER', 'GY': 'OTHER', 'PY': 'OTHER', 'PE': 'OTHER', 'SR': 'OTHER', 'UY': 'OTHER', 'VE': 'OTHER'}



# load data
with open('dataset/user_games_4.json', 'r') as f:
    data = json.load(f)
user_data = data['user_games']

print(user_data[0])

digits = datasets.load_digits()

gameList = {}
targets = []
datas = []

# get 100 most played game
for user in user_data:
    if user[1]['game_count'] > 0:
        for game in user[1]['games']:
            if gameList.get(game['appid']) == None:
                gameList.update({game['appid']: game['playtime_forever']})
            else:
                gameList[game['appid']] += game['playtime_forever']

# sorted top 100 games by playtime
gameList = dict(sorted(gameList.items(), key=lambda item:item[1], reverse=True))
# reserve top 100 games
gameList = dict(islice(gameList.items(), 0, 100))
# save as list
gameList = list(gameList.keys())
print(gameList)
# print(10 in gameList)


# test
# l = [0] * 100
# print(l)
# for i in user_data[0][1]['games']:
#     if i['appid'] in gameList:
#         l[gameList.index(i['appid'])] = i['playtime_forever']
#         print(gameList.index(i['appid']))
# print(l)
# test

# for i in data:
#     target[n] = country2continent[i[0]['loccountrycode']]
for user in user_data:
    # print(user[0]['timecreated'])
    targets.append(country2continent[user[0]['loccountrycode']])
    data = [0] * 101
    data.append(user[1]['game_count'])
    # print(user)
    if user[1]['game_count'] > 0:
        for game in user[1]['games']:
            if game['appid'] in gameList:
                data[gameList.index(game['appid'])] = game['playtime_forever']
    datas.append(data)

# print(datas)
# n = 0
# for i in datas:
#     print(n)
#     print(i)
#     n += 1

# split train- and test dataset
x = datas
y = targets
x_train, x_test, y_train, y_test = tts(x, y, test_size=0.1)

# learning
# clf = svc()
# n_estimators=300, learning_rate=0.8
clf = AdaBoostClassifier()
clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)

print(classification_report(y_test, y_pred))
sns.heatmap(confusion_matrix(y_test, y_pred))
#

# atterbus
# pipe = Pipeline([('scaler', MinMaxScaler()), ('clf', svc())]) test with/without MinMaxScaler()
# randomcv

params = dict(
    scaler = [None, MinMaxScaler()],
    clf__kernel = ['rbf'],
    clf__C = [0.1, 0.2, 0.3, 0.5, 1.0, 10, 100],
    clf__gamma = [1E-3, 1E-2, 1E-1, 1.0],
)

pipe = Pipeline([('scaler', MinMaxScaler()), ('clf', svc())])
# pipe = Pipeline([('scaler', MinMaxScaler()), ('clf', AdaBoostClassifier())])
grid_search = GridSearchCV(pipe, param_grid=params, cv=5)

grid_search.fit(x_train, y_train)

predictions = grid_search.predict(x_test)
print(classification_report(y_test, predictions))
# sns.heatmap(confusion_matrix(y_test, predictions))



# precision = TP / (TP + FP)
# recall = TP / (TP + FN)
# accuracy = (TP + TN) / (TP + FP + TN + FN)

# adaboost
# confusion_matrix()
# randomizeCV

#               precision    recall  f1-score   support
# /usr/local/lib/python3.6/site-packages/sklearn/metrics/classification.py:1135: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples.
#   'precision', 'predicted', average, warn_for)
#
#          AS       0.50      0.00      0.01       241
#          EU       0.47      1.00      0.64       914
#          NA       0.40      0.00      0.01       553
#       OTHER       0.00      0.00      0.00       235
#
# avg / total       0.40      0.47      0.30      1943
#
#              precision    recall  f1-score   support
#
#          AS       0.33      0.01      0.02       258
#          EU       0.48      0.99      0.64       922
#          NA       0.38      0.01      0.01       545
#       OTHER       0.00      0.00      0.00       218
#
# avg / total       0.37      0.47      0.31      1943
#
#              precision    recall  f1-score   support
#
#          AS       1.00      0.01      0.02       255
#          EU       0.47      1.00      0.64       906
#          NA       0.33      0.00      0.00       536
#       OTHER       0.50      0.00      0.01       246
#

# dataset4
# # precision    recall  f1-score   support
#
#          AS       1.00      0.01      0.02       246
#          EU       0.50      1.00      0.66       960
#          NA       0.25      0.00      0.00       518
#       OTHER       0.20      0.00      0.01       219
#
# avg / total       0.46      0.49      0.33      1943
#
#              precision    recall  f1-score   support
#
#          AS       0.44      0.15      0.23       246
#          EU       0.53      0.88      0.66       960
#          NA       0.50      0.24      0.32       518
#       OTHER       0.08      0.00      0.01       219
#
# avg / total       0.46      0.52      0.44      1943

# data7
#  precision    recall  f1-score   support
#
#          AS       0.12      0.00      0.01       211
#          EU       0.45      1.00      0.62       600
#          NA       0.00      0.00      0.00       338
#       OTHER       0.00      0.00      0.00       181
#
# avg / total       0.22      0.45      0.28      1330
#
#              precision    recall  f1-score   support
#
#          AS       0.52      0.11      0.18       211
#          EU       0.47      0.93      0.63       600
#          NA       0.50      0.15      0.23       338
#       OTHER       0.25      0.01      0.01       181
#
# avg / total       0.46      0.48      0.37      1330

# pca