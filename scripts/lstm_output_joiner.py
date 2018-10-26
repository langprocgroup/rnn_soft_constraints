
import os
import pandas as pd

exp_paths = [
  "particleshift/tests/",
  "gardenpathing-verb-ambiguity/tests/",
  "gardenpathing-animacy/tests/",
  "binding-gender/tests/",
  "src_orc/tests/",
  "obligatory-upcoming-dependencies/english_npi/tests/",
  "obligatory-upcoming-dependencies/subordination/tests/"
]

prefix = "../"

def word_is_unk(items):
  return any([p in {"<unk>", "<UNK>"} for p in items])

def equal_cols(col1, col2):
  for x in range(len(col1)):
    if col1[x] != col2[x] and not word_is_unk([col1[x], col2[x]]):
      print(col1[x])
      print(col2[x])
      return False
  return True


for p in exp_paths:
  dataframes = []
  for filename in os.listdir(prefix + p):
    if ".tsv" in filename and "-output" not in filename and "combined" not in filename:
      print(filename)
      exp_columns = ["sent_index", "word_index", "word", "region", "condition"]
      lstm_result_columns = ["word_glstm", "surprisal"]

      # Experiment data (region, sentence number, etc...)
      exp_data = pd.read_csv(prefix+p+filename, sep="\t", header=None, names=exp_columns)

      # Google LSTM Results
      glstm_results = pd.read_csv(prefix+p+filename.split(".")[0]+"-output.tsv", sep="\t", header=None, names=lstm_result_columns)
      google_result = exp_data.join(glstm_results, rsuffix='_other')
      google_result["LSTM"] = "google-1b"
      assert equal_cols(google_result.word.tolist(),google_result.word_glstm.tolist()), "Google Word columns are not equal"
      
      # Wiki (Gulordava) LSTM Results
      wlstm_results = pd.read_csv(prefix+p+filename.split(".")[0]+"-output_wiki.tsv", sep="\t", header=None, names=lstm_result_columns)
      wiki_result = exp_data.join(wlstm_results, rsuffix='_other')
      wiki_result["LSTM"] = "gulordava-wiki"
      assert equal_cols(wiki_result.word.tolist(),wiki_result.word_glstm.tolist()), "Wiki Word columns are not equal"


      combined_result = pd.concat([google_result, wiki_result]).sort_index().reset_index()
      dataframes.append(combined_result)

  export = pd.concat(dataframes)
  export.to_csv(prefix + p + "combined_results.tsv", sep="\t")










