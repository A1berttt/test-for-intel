import numpy as np
import pandas as pd
import daal4py as d4p
from conf import args
from sklearn.model_selection import ParameterGrid
pd.options.mode.chained_assignment = None


def daal_model(df):
    TRAIN_SIZE, TEST_SIZE, PRED_SIZE = int(args.row_count * 0.8), int(args.row_count * 0.1), int(args.row_count * 0.1)
    train_df, test_df, pred_df = df.iloc[:TRAIN_SIZE], df.iloc[TRAIN_SIZE: TRAIN_SIZE + TEST_SIZE], df.iloc[-PRED_SIZE:]
    train_x, train_y = train_df[args.src_cols], train_df[args.tgt_col]
    test_x, test_y = test_df[args.src_cols], test_df[args.tgt_col]
    pred_x = pred_df[args.src_cols]
    best_score = float("inf")
    best_params = None
    params_grid = ParameterGrid(args.daal_params_grid)
    for params in params_grid:
        model = d4p.gbt_regression_training(**params)
        train_result = model.compute(train_x, train_y)
        predict_alg = d4p.gbt_regression_prediction()
        pred = predict_alg.compute(test_x, train_result.model).prediction
        score = (np.mean(abs(pred - test_y.values) / test_y.values))
        if score < best_score:
            best_score = score
            best_params = params
    best_model = d4p.gbt_regression_training(**best_params)
    best_train_result = best_model.compute(df.iloc[:TRAIN_SIZE + TEST_SIZE][args.src_cols], df.iloc[:TRAIN_SIZE + TEST_SIZE][args.tgt_col])
    best_predict_alg = d4p.gbt_regression_prediction()
    pred_df['pred'] = best_predict_alg.compute(pred_x, best_train_result.model).prediction
    return pred_df
