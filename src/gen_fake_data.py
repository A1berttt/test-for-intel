import os
import shutil
import multiprocessing
import numpy as np
import pandas as pd
from conf import args


def gen_data(idx, columns):
    ROW_CNT = args.row_count
    COL_CNT = 51
    df = pd.DataFrame(np.random.randn(ROW_CNT, COL_CNT), columns=columns)
    df.to_csv(os.path.join(args.input_path, '%04d.csv' % idx), index=0)


def main():
    columns = ['col_%02d' % i for i in range(51)]

    if os.path.exists(args.input_path):
        shutil.rmtree(args.input_path)
    os.makedirs(args.input_path)

    pool = multiprocessing.Pool(processes=min(multiprocessing.cpu_count(), args.total_file_counts))
    for i in range(args.total_file_counts):
        pool.apply_async(gen_data, (i, columns))
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
