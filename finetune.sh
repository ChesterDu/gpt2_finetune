cd /opt/repo/gpt2_finetune/
pip install --upgrade pip
pip install -r requirements.txt
python download_model.py 124M
# cd src
# python src/main.py --model_dir "./models/124M" \
#                    --data_name "./kg" \
#                    --data_dir "./data" \

# python src/main.py --is_train 0 \ --cond 0 \--model_dir models/124M \--batch_size 50 \--data_name kg \--data_dir data