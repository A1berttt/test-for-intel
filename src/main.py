import os
import sys
import time
import shutil
import multiprocessing
from conf import args
from model import run_model


def main():

    # Output Paths
    if os.path.exists(args.output_path):
        shutil.rmtree(args.output_path)
    os.mkdir(args.output_path)

    # Running Model
    pool = multiprocessing.Pool(processes=min(multiprocessing.cpu_count(), args.total_file_counts))
    results = []
    for i in range(args.total_file_counts):
        results.append(pool.apply_async(run_model, (i, )))
    pool.close()
    pool.join()
    df_results = [res.get() for res in results]

    # Timing
    read_time_sum = sum([t[1] for t in df_results])
    run_time_sum = sum(t[2] for t in df_results)
    run_mm, run_ss = divmod(run_time_sum, 60)
    run_time_ave = run_time_sum / args.total_file_counts
    run_mm_ave, run_ss_ave = divmod(run_time_ave, 60)
    write_time_sum = sum(t[3] for t in df_results)
    sys.stdout.write('===> Processing Prediction Results.\n')
    sys.stdout.write('===> Saving Prediction Results.\n')
    sys.stdout.write('===> Reading Totally Costs %f sec.\n' % read_time_sum)
    sys.stdout.write('===> Running Totally Costs %d min, %d sec.\n' % (run_mm, run_ss))
    sys.stdout.write('===> Writing Totally Costs %f sec.\n' % write_time_sum)
    sys.stdout.write('===> Reading Averagely Costs %f sec.\n' % (read_time_sum / args.total_file_counts))
    sys.stdout.write('===> Running Averagely Costs %d min, %d sec.\n' % (run_mm_ave, run_ss_ave))
    sys.stdout.write('===> Writing Averagely Costs %f sec.\n' % (write_time_sum / args.total_file_counts))


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time =int(end_time - start_time)
    mm, ss = divmod(elapsed_time, 60)
    sys.stdout.write('Used: %2d min, %2d sec.\n' % (mm, ss))
