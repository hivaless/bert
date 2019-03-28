import run_pretraining as pt
import tensorflow as tf

cmd_line_args = 'cmd --input_file=/Users/kakao/AI/nlp_projects/data/hangul/brunch-sample.tfrecord \
  --output_dir=/Users/kakao/AI/nlp_projects/data/bert_hangul_model \
  --do_train=True \
  --do_eval=True \
  --bert_config_file=bert_config/bert_config_small.json \
  --train_batch_size=32 \
  --max_seq_length=512 \
  --max_predictions_per_seq=77 \
  --num_train_steps=200 \
  --num_warmup_steps=10 \
  --learning_rate=2e-5'
argv = [arg.strip() for arg in cmd_line_args.split(' ')]
tf.app.run(pt.main, argv)

