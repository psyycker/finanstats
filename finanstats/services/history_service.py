import calendar
import datetime

import numpy as np
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from finanstats.daos.history_dao import HistoryDao
from finanstats.services.ticker_service import TickerService
import pandas as pd


def is_up_to_date(date):
    now = datetime.date.today()
    if now.weekday() < calendar.SATURDAY:
        compare_date = now
    else:
        days_since_last_friday = (now.weekday() - calendar.FRIDAY + 7) % 7
        compare_date = now - datetime.timedelta(days=days_since_last_friday)

    return date == compare_date


def fetch_history(ticker):
    dao = HistoryDao()
    ticker = TickerService(ticker)
    most_recent = dao.get_most_recent_data_point(ticker.get_ticker_code())
    history = None
    if most_recent is not None and is_up_to_date(most_recent[0]) is False:
        date = most_recent[0]
        history = ticker.get_history_from(date)
    elif most_recent is None:
        history = ticker.get_history()

    if history is not None:
        dao.create_dividends_from_series(history, ticker.get_ticker_code())
    else:
        print(f"skip {ticker.get_ticker_code()}")


def linear_regression(ticker):
    dao = HistoryDao()
    rows = dao.get_all_history_for_ticker(ticker)
    data = [row for row in rows]
    df = pd.DataFrame(data, columns=['date', 'open', 'close', 'high', 'low', 'volume'])
    df['date'] = pd.to_datetime(df['date'])  # convert the 'date' column to datetime type

    X = df.drop('close', axis=1)
    y = df['close']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    # Preserve dates for later use (and remove from feature set)
    X_test_dates = X_test['date']
    X_train = X_train.drop('date', axis=1)
    X_test = X_test.drop('date', axis=1)

    # Train the model
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    # Make predictions on the test data
    y_pred = regressor.predict(X_test)

    # Calculate and display error metrics
    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
    print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

    # Create a DataFrame comparing actual and predicted prices
    df_compare = pd.DataFrame({'Date': X_test_dates, 'Actual': y_test, 'Predicted': y_pred})

    # Sort the DataFrame by date
    df_compare.sort_values('Date', inplace=True)

    # Print the comparison DataFrame
    print(df_compare)
