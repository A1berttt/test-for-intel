import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--model', type=str, default='xgb', choices=['xgb', 'daal'])
parser.add_argument('--input_path', type=str, default='../datasets/splits')
parser.add_argument('--output_path', type=str, default='../results')
parser.add_argument('--xgb_params_grid', type=dict, default={
    "n_estimators": range(50, 110, 10),
    "max_depth": range(3, 7),
    "min_child_weight": range(1, 4),
    "random_state": [0],
    "n_jobs": [1],
})
parser.add_argument('--daal_params_grid', type=dict, default={
    "maxIterations": range(100, 501, 100),
    "maxTreeDepth": range(3, 7),
    "minObservationsInLeafNode": range(1, 4),
})
parser.add_argument('--src_cols', type=list, default=[
    'col_00', 'col_01', 'col_02', 'col_03', 'col_04', 'col_05', 'col_06', 'col_07', 'col_08', 'col_09',
    'col_10', 'col_11', 'col_12', 'col_13', 'col_14', 'col_15', 'col_16', 'col_17', 'col_18', 'col_19',
    'col_20', 'col_21', 'col_22', 'col_23', 'col_24', 'col_25', 'col_26', 'col_27', 'col_28', 'col_29',
    'col_30', 'col_31', 'col_32', 'col_33', 'col_34', 'col_35', 'col_36', 'col_37', 'col_38', 'col_39',
    'col_40', 'col_41', 'col_42', 'col_43', 'col_44', 'col_45', 'col_46', 'col_47', 'col_48', 'col_49',
])
parser.add_argument('--tgt_col', type=str, default='col_50')
parser.add_argument('--total_file_counts', type=int, default=10)
parser.add_argument('--row_count', type=int, default=1000)

args = parser.parse_args()