
import pandas as pd
import csv

def words_with_regions(df, regions, c):   
  result = []
  for row in range(df.shape[0]):
    sentence = []
    for region in regions:
      string = df.ix[row, region]
      words = string.strip().split()
      sentence.extend([(row, word,region, c) for word in words])

    # To get word position in sentence
    sentence = [(sentence[i][0], i, sentence[i][1], sentence[i][2], sentence[i][3]) for i in range(len(sentence))]
    result.append(sentence)
  return result 


def write_items(filename, filepath, df):
  for k,v in conditions.items():
    result = words_with_regions(df, v, k)
    sents = [" ".join(x[2] for x in r).replace("’", "'") for r in result]
    with open(filepath+"tests/"+k+".txt", "w") as f:
      f.writelines([x + "\n" for x in sents])
    with open(filepath+"tests/"+k+".tsv", 'w') as f:
      f.writelines("\t".join(str(x) for x in w)+"\n" for sent in result for w in sent)

# ======================
# === Binding And Gender ===
# CHECK FOR EOS IN ALL OF THEM!
conditions = {
  "refl_match" : ["Antecedent","Matrix Clause","Reflexive Match","End"],
  "refl_mismatch" : ["Antecedent","Matrix Clause","Reflexive Mismatch","End"],
  "refl_match_rc_match" : ["Antecedent","Relative Clause","RC Object Match","Matrix Clause","Reflexive Match","End"],
  "refl_match_rc_mismatch" : ["Antecedent","Relative Clause","RC Object Match","Matrix Clause","Reflexive Mismatch","End"],
  "refl_mismatch_rc_match" : ["Antecedent","Relative Clause","RC Object Mismatch","Matrix Clause","Reflexive Match","End"],
  "refl_mismatch_rc_mismatch" : ["Antecedent","Relative Clause","RC Object Mismatch","Matrix Clause","Reflexive Mismatch","End"]
}

filepath = "../binding-gender/"
filename = "antecedent-match-and-rc-intervener"
df = pd.read_excel(filepath+filename+".xlsx", header=1)
write_items(filename, filepath, df)

# ======================
# === Gardenpathing ====
# ======================

# A) -- Animacy --
conditions = {
  "animate_reduced" : ["Start","Animate noun","verb","by-phrase","main verb","End"],
  "inanimate_reduced" : ["Start","Inanimate noun","verb","by-phrase","main verb","End"],
  "animate_unreduced" : ["Start","Animate noun","that-was","verb","by-phrase","main verb","End"] ,
  "inanimate_unreduced" : ["Start","Inanimate noun","that-was","verb","by-phrase","main verb","End"]
}

filename = "reduction-and-matrix-subj-animacy"
filepath = "../gardenpathing-animacy/"
df = pd.read_excel(filepath+filename+".xlsx", header=0)
write_items(filename, filepath, df)

# ======================
# B) -- Ambiguity --
conditions = {
  "ambig_reduced" : ["Start","Noun","Ambiguous verb","RC contents","Disambiguator","End"],
  "ambig_unreduced" : ["Start","Noun","Unreduced content","Ambiguous verb","RC contents","Disambiguator","End"],
  "unambig_reduced" : ["Start","Noun","Unambiguous verb","RC contents","Disambiguator","End"],
  "unambig_unreduced" : ["Start","Noun","Unreduced content","Unambiguous verb","RC contents","Disambiguator","End"]
}

filename = "verb-ambiguity-with-intervening-phrase"
filepath = "../gardenpathing-verb-ambiguity/"
df = pd.read_excel(filepath+filename+".xlsx", header=0)
write_items(filename, filepath, df)

# ======================
# === English NPIs ===
conditions = {
  "neg-attractor_rc-ever" : ["Negative Liscensor", "Subject", "Distractor RC", "Matrix Ever", "Conclusion"],
  "neg-attractor_rc-any" : ["Negative Liscensor", "Subject", "Distractor RC", "Matrix Any", "Conclusion"],
  "neg-attractor_rc-plain" : ["Negative Liscensor", "Subject", "Distractor RC", "Matrix Plain", "Conclusion"],
  "neg-plain_rc-ever" : ["Negative Liscensor", "Subject", "RC", "Matrix Ever", "Conclusion"],
  "neg-plain_rc-any" : ["Negative Liscensor", "Subject", "RC", "Matrix Any", "Conclusion"],
  "neg-plain_rc-plain" : ["Negative Liscensor", "Subject", "RC", "Matrix Plain", "Conclusion"],
  "pos-attractor_rc-ever" : ["Non-Negative Liscensor", "Subject", "Distractor RC", "Matrix Ever", "Conclusion"],
  "pos-attractor_rc-any" : ["Non-Negative Liscensor", "Subject", "Distractor RC", "Matrix Any", "Conclusion"],
  "pos-attractor_rc-plain" : ["Non-Negative Liscensor", "Subject", "Distractor RC", "Matrix Plain", "Conclusion"],
  "pos-plain_rc-ever" : ["Non-Negative Liscensor", "Subject", "RC", "Matrix Any", "Conclusion"],
  "pos-plain_rc-plain" : ["Non-Negative Liscensor", "Subject", "RC", "Matrix Plain", "Conclusion"]
}

conditions = {
  "neg-prc-ever-any" : ["Negative Liscensor", "Subject", "RC", "Aux", "Ever", "Verb", "Any", "Noun", "Continuation", "Conclusion"],
  "neg-prc-never-any" : ["Negative Liscensor", "Subject", "RC", "Aux", "Verb", "Any", "Noun", "Continuation", "Conclusion"],
  "neg-prc-ever-nany" : ["Negative Liscensor", "Subject", "RC", "Aux", "Ever", "Verb", "Noun", "Continuation", "Conclusion"],
  "neg-prc-never-nany" : ["Negative Liscensor", "Subject", "RC", "Aux", "Verb", "Noun", "Continuation", "Conclusion"],
  "neg-nprc-ever-any" : ["Negative Liscensor", "Subject", "Distractor RC", "Aux", "Ever", "Verb", "Any", "Noun", "Continuation", "Conclusion"],
  "neg-nprc-never-any" : ["Negative Liscensor", "Subject", "Distractor RC", "Aux", "Verb", "Any", "Noun", "Continuation", "Conclusion"],
  "neg-nprc-ever-nany" : ["Negative Liscensor", "Subject", "Distractor RC", "Aux", "Ever", "Verb", "Noun", "Continuation", "Conclusion"],
  "neg-nprc-never-nany" : ["Negative Liscensor", "Subject", "Distractor RC", "Aux", "Verb", "Noun", "Continuation", "Conclusion"],
  "pos-prc-ever-any" : ["Non-Negative Liscensor", "Subject", "RC", "Aux", "Ever", "Verb", "Any", "Noun", "Continuation", "Conclusion"],
  "pos-prc-never-any" : ["Non-Negative Liscensor", "Subject", "RC", "Aux", "Verb", "Any", "Noun", "Continuation", "Conclusion"],
  "pos-prc-ever-nany" : ["Non-Negative Liscensor", "Subject", "RC", "Aux", "Ever", "Verb", "Noun", "Continuation", "Conclusion"],
  "pos-prc-never-nany" : ["Non-Negative Liscensor", "Subject", "RC", "Aux", "Verb", "Noun", "Continuation", "Conclusion"],
  "pos-nprc-ever-any" : ["Non-Negative Liscensor", "Subject", "Distractor RC", "Aux", "Ever", "Verb", "Any", "Noun", "Continuation", "Conclusion"],
  "pos-nprc-never-any" : ["Non-Negative Liscensor", "Subject", "Distractor RC", "Aux", "Verb", "Any", "Noun", "Continuation", "Conclusion"],
  "pos-nprc-ever-nany" : ["Non-Negative Liscensor", "Subject", "Distractor RC", "Aux", "Ever", "Verb", "Noun", "Continuation", "Conclusion"],
  "pos-nprc-never-nany" : ["Non-Negative Liscensor", "Subject", "Distractor RC", "Aux", "Verb", "Noun", "Continuation", "Conclusion"],
}

filename = "npi-distractor"
filepath = "../obligatory-upcoming-dependencies/english_npi/"
df = pd.read_excel(filepath+filename+".xlsx", header=1)
write_items(filename, filepath, df)

# ======================
# === Subordination ====

conditions = {
  "sub-matrix" : ["Subordinator","Subordinate clause 1","Subordinate clause 2","Main clause","Conclusion"],
  "sub-no_matrix" : ["Subordinator","Subordinate clause 1","Subordinate clause 2","Conclusion"],
  "no_sub-matrix" : ["Subordinate clause 1","Subordinate clause 2","Main clause","Conclusion"],
  "no_sub-no_matrix" : ["Subordinate clause 1","Subordinate clause 2","Conclusion"]
}

first_sc = ["Subordinate clause PP 1", "Subordinate clause SRC 1", "Subordinate clause ORC 1"]
second_sc = ["Subordinate clause PP 2", "Subordinate clause SRC 2", "Subordinate clause ORC 2"]

for i in range(len(first_sc)):
  c = {
    "sub-1sc"+str(i+1)+"-matrix" : ["Subordinator","Subordinate clause 1",first_sc[i],"Subordinate clause 2","Main clause","Conclusion"],
    "sub-1sc"+str(i+1)+"-no_matrix" : ["Subordinator","Subordinate clause 1",first_sc[i],"Subordinate clause 2","Conclusion"],
    "no_sub-1sc"+str(i+1)+"-matrix" : ["Subordinate clause 1",first_sc[i],"Subordinate clause 2","Main clause","Conclusion"],
    "no_sub-1sc"+str(i+1)+"-no_matrix" : ["Subordinate clause 1",first_sc[i],"Subordinate clause 2","Conclusion"]
  }
  conditions.update(c)

for i in range(len(second_sc)):
  c = {
    "sub-2sc"+str(i+1)+"-matrix" : ["Subordinator","Subordinate clause 1","Subordinate clause 2",second_sc[i],"Main clause","Conclusion"],
    "sub-2sc"+str(i+1)+"-no_matrix" : ["Subordinator","Subordinate clause 1","Subordinate clause 2",second_sc[i],"Conclusion"],
    "no_sub-2sc"+str(i+1)+"-matrix" : ["Subordinate clause 1","Subordinate clause 2",second_sc[i],"Main clause","Conclusion"],
    "no_sub-2sc"+str(i+1)+"-no_matrix" : ["Subordinate clause 1","Subordinate clause 2",second_sc[i],"Conclusion"]
  }
  conditions.update(c)

for i in range(len(first_sc)):
  for j in range(len(second_sc)):
    c = {
      "sub-1sc"+str(i+1)+"-2sc"+str(j+1)+"-matrix" : ["Subordinator","Subordinate clause 1",first_sc[i],"Subordinate clause 2",second_sc[i],"Main clause","Conclusion"],
      "sub-1sc"+str(i+1)+"-2sc"+str(j+1)+"-no_matrix" : ["Subordinator","Subordinate clause 1",first_sc[i],"Subordinate clause 2",second_sc[i],"Conclusion"],
      "no_sub-1sc"+str(i+1)+"-2sc"+str(j+1)+"-matrix" : ["Subordinate clause 1",first_sc[i],"Subordinate clause 2",second_sc[i],"Main clause","Conclusion"],
      "no_sub-1sc"+str(i+1)+"-2sc"+str(j+1)+"-no_matrix" : ["Subordinate clause 1",first_sc[i],"Subordinate clause 2",second_sc[i],"Conclusion"]
    }
    conditions.update(c)

filename = "subordination"
filepath = "../obligatory-upcoming-dependencies/subordination/"
df = pd.read_excel(filepath+filename+".xlsx", header=0)
write_items(filename, filepath, df)


# ======================
# === SRC / ORC ===

conditions = {
  "subj_rc": ["NP1", "Reletivizer", "Verb", "NP2", "Outer VP", "End"],
  "obj_rc" : ["NP1", "Reletivizer", "NP2", "Verb", "Outer VP", "End"],
  "pronoun_subj" : ["Pronoun", "Verb", "NP2", "End"],
  "np_subj": ["NP1", "Verb", "NP2", "End"],
  "np_pp_subj" : ["NP1", "PP modifier", "Verb", "NP2", "End"],
  "np_rc_subj" : ["NP1", "RC modifier", "Verb", "NP2", "End"],
  "np_prnoun_rc" : ["NP2", "Reletivizer", "Pronoun", "Verb", "Outer VP", "End"],
  "np_np_rc" : ["NP2", "Reletivizer", "NP1", "Verb", "Outer VP", "End" ],
  "np_np_pp_rc" : ["NP2", "Reletivizer", "NP1", "PP modifier", "Verb", "Outer VP", "End" ],
  "np_np_rc_rc" : ["NP2", "Reletivizer", "NP1",  "RC modifier", "Verb", "Outer VP", "End" ]
}

filename = "src_orc"
filepath = "../src_orc/"
df =pd.read_excel(filepath+filename+".xlsx", header=0)
write_items(filename, filepath, df)

# ======================
# === Particle Shift ===
conditions = {
  "long_shifted" : ['Subject NP', "Verb", "Modifier Long", "Particle", "End"],
  "short_shifted" : ["Subject NP", "Verb", "Modifier Short", "Particle", "End"],
  "long_unshifted" : ["Subject NP", "Verb", "Particle", "Modifier Long", "End"],
  "short_unshifted" : ["Subject NP", "Verb", "Particle", "Modifier Short", "End"]
}

filename = "particle-shift"
filepath = "../particleshift/"
df = pd.read_excel(filepath+filename+".xlsx", header=1)
write_items(filename, filepath, df)


