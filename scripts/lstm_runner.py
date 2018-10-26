
# Script for running the google 1b lstm on a series of subdirectories.

import os

final_folder_paths = [
  "obligatory-upcoming-dependencies/english_npi/tests/",
  "gardenpathing-verb-ambiguity/tests/",
  "gardenpathing-animacy/tests/",
  "binding-gender/tests/",
  "obligatory-upcoming-dependencies/subordination/tests/",
  "src_orc/tests/"]

prefix = "../../rnnpsycholing/"



sub_files = []

def run_files(filenames, prefix):
  for f in filenames:
    filename = f[:-4]
    print("-----")
    print(filename)
    command = "python eval_test_google.py \
                  --pbtxt ../data/graph-2016-09-10.pbtxt \
                  --ckpt '../data/ckpt-*' \
                  --vocab_file ../data/vocab-2016-09-10.txt \
                  --output_file " + prefix + sub + filename + "-output.tsv \
                  --input_file " + prefix + sub + filename + ".txt"
    os.system(command)

def run_directories(directories, prefix):
  for p in directories:
    for file in os.listdir(prefix + p):
      if ".txt" in file:
        print("------")
        print(file)
        filename = file.split(".")[0]
        command = "python eval_test_google.py \
                  --pbtxt ../data/graph-2016-09-10.pbtxt \
                  --ckpt '../data/ckpt-*' \
                  --vocab_file ../data/vocab-2016-09-10.txt \
                  --output_file " + prefix + p + filename + "-output.tsv \
                  --input_file " + prefix + p + filename + ".txt"
        os.system(command)

src_orc = ["src_orc/tests/"]

#run_directories(src_orc, prefix)
run_files(sub_files, prefix)



