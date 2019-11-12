RUN_DIR=`dirname $0`
cd $RUN_DIR
python gen_fake_data.py
python main.py