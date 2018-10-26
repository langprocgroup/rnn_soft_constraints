Scripts
=======


Usage of `evaluate_target_word_test.py` with the Gulordava et al. (2018) LSTM:
* `git clone https://github.com/facebookresearch/colorlessgreenRNNs`
* Put `evaluate_target_word_test.py` in `colorlessgreenRNNs/src/language_models`
* From the directory `colorlessgreenRNNs/src`, run it as:
```{python3}
`python language_models/evaluate_target_word_test.py --checkpoint hidden650_batch128_dropout0.2_lr20.0.pt --surprisalmode True --data ../data/lm/English --prefixfile path/to/test/sentences --outf path/to/desired/results/file`
```

Usage of `eval_test_google.py` with Google's 1-billion LSTM (2016)
* Follow instructions on `https://github.com/tensorflow/models/tree/master/research/lm_1b`
* put `eval_test_google.py` in `/lm_1b`
* From the directory `/lm_1b` run it as:
```{python3}
`python eval_test_google.py --pbtxt ../data/graph-2016-09-10.pbtxt --ckpt '../data/ckpt-*' --vocab_file ../data/vocab-2016-09-10.txt --output_file your/output/file/here.txt --input_file your/input/file.txt`
```

To Generate and Run Google LSTM outputs:
* From /scripts/ run `test_sentence_builder.py` to turn .xlsx files into .txt test sentences and generate .tsv files with word/sentene/region information
* From /scripts/ run `run_models.py` to generate surprisal outputs for each word and join the data with previous .tsv files