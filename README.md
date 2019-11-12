# test-for-intel

## Test Code For Xgboost or Daal-Gbt-Reg

---
1. Generate Fake Data.
2. Run the Model.
3. Please Make Sure You Have Installed Pkgs for pandas, sklearn, numpy, xgboost, daal4py(only for daal-gbt-reg).

### Examples

---
- generate fake data
```
$ python gen_fake_data.py
``` 
- run xgboost model
```
$ python main.py
```
- run daal model
```
$ python main.py --mode daal
``` 

### Guide

---
| arg | explanation |
| :---- | :---- |
| --model | xgb or daal |
| --input_path | input files dir |
| --output_path | output files dir |
| --xgb_params_grid | params of xgb model |
| --daal_params_grid | params of daal model |
| --src_cols | columns for training |
| --tgt_cols | label for training |
|--total_file_counts | counts of files for testing |

### Attention !

---
- If the version of you xgboost < 1.0, it will display xgb objective warning, please run
```angular2
$ python -W ignore main.py
```
