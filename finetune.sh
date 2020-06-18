cd /opt/repo/gpt2_finetune/src
pip install --upgrade pip
pip install -r ../requirements.txt
python download_model.py 124M
python main.py --is_train 1 --cond 0 --model_dir models/124M --batch_size 50 --data_name kg --data_dir data
python main.py --is_train 0 --cond 0 --model_dir models/124M --batch_size 20 --data_name kg --data_dir data