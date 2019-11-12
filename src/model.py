import os
import sys
import time
import pandas as pd
from conf import args
pd.options.mode.chained_assignment = None



def run_model(file_idx):

    # Read
    file_name = os.path.join(args.input_path, '%04d.csv' % file_idx)
    read_start_time = time.time()
    df = pd.read_csv(file_name)
    read_end_time = time.time()
    read_elapsed_time = read_end_time - read_start_time
    sys.stdout.write('===> Reading Files Costs %f sec.\n' % read_elapsed_time)

    # Run
    if args.model == 'xgb':
        from xgb_model import xgb_model
        model = xgb_model
    elif args.model == 'daal':
        from daal_model import daal_model
        model = daal_model
    else:
        sys.stderr.write('[Model Error!] Please choose correct model.\n')
        sys.exit(1)
    run_start_time = time.time()
    res_df = model(df)
    run_end_time = time.time()
    run_elapsed_time = run_end_time - run_start_time
    sys.stdout.write('===> Running Model Costs %d sec.\n' % run_elapsed_time)

    # Write
    write_start_time = time.time()
    output_file_name = os.path.join(args.output_path, '%04d.csv' % file_idx)
    res_df.to_csv(output_file_name, index=0)
    write_end_time = time.time()
    write_elapsed_time = write_end_time - write_start_time
    sys.stdout.write('===> Writing Files Costs %f sec.\n' % write_elapsed_time)

    sys.stdout.write('===> Finished Processing File: %04d.\n' % file_idx)

    return [res_df, read_elapsed_time, run_elapsed_time, write_elapsed_time]
