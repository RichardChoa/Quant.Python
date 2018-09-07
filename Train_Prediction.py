# Author: Richard
# DATE:2018/9/6
# -*- coding: utf-8 -*-


from Features_Extract import extract_featuresets
from sklearn import svm, neighbors
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier, RandomForestClassifier
from collections import Counter
import warnings


def do_ml(ticker):
    X, y, df = extract_featuresets(ticker)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25
    )

    # clf = neighbors.KNeighborsClassifier()
    clf = VotingClassifier([('lsvc', svm.LinearSVC()),
                            ('knn', neighbors.KNeighborsClassifier()),
                            ('rfor', RandomForestClassifier())])

    clf.fit(X_train, y_train)

    prediction = clf.predict(X_test)
    confidence = clf.score(X_test, y_test)

    print('predicted class count:', Counter(prediction))
    print('accuracy:', confidence)


if __name__ == '__main__':
    warnings.filterwarnings(action='ignore', category= DeprecationWarning)
    do_ml('MMM')
