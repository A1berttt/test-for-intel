import numpy as np
import pandas as pd
import xgboost as xgb
from conf import args
from sklearn.model_selection import ParameterGrid
pd.options.mode.chained_assignment = None


def xgb_model(df):
    TRAIN_SIZE, TEST_SIZE, PRED_SIZE = int(args.row_count * 0.8), int(args.row_count * 0.1), int(args.row_count * 0.1)
    train_df, test_df, pred_df = df.iloc[:TRAIN_SIZE], df.iloc[TRAIN_SIZE: TRAIN_SIZE + TEST_SIZE], df.iloc[-PRED_SIZE:]
    train_x, train_y = train_df[args.src_cols], train_df[args.tgt_col]
    test_x, test_y = test_df[args.src_cols], test_df[args.tgt_col]
    pred_x = pred_df[args.src_cols]
    best_score = float("inf")
    best_params = None
    params_grid = ParameterGrid(args.xgb_params_grid)
    for params in params_grid:
        model = xgb.XGBRegressor(**params)
        model.fit(train_x, train_y)
        pred = model.predict(test_x)
        score = np.mean(abs(pred - test_y.values) / test_y.values)
        if score < best_score:
            best_score = score
            best_params = params
    best_model = xgb.XGBRegressor(**best_params)
    best_model.fit(df.iloc[:TRAIN_SIZE + TEST_SIZE][args.src_cols], df.iloc[:TRAIN_SIZE + TEST_SIZE][args.tgt_col])
    pred_df['pred'] = best_model.predict(pred_x)
    return pred_df
