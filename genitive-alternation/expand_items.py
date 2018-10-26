import os
import sys

import pandas as pd

conditions = {
    's_indef_short': ['Indef Possessor', 'S', 'Possessum'],
    's_indef_long': ['Indef Possessor', 'Possessor Modifier', 'S', 'Possessum'],
    's_def_short': ['Def Possessor', 'S', 'Possessum'],
    's_def_long': ['Def Possessor', 'Possessor Modifier', 'S', 'Possessum'],
    'of_indef_short': ['the', 'Possessum', 'of', 'Indef Possessor'],
    'of_indef_long': ['the', 'Possessum', 'of', 'Indef Possessor', 'Possessor Modifier'],
    'of_def_short': ['the', 'Possessum', 'of', 'Def Possessor'],
    'of_def_long': ['the', 'Possessum', 'of', 'Def Possessor', 'Possessor Modifier'],
}
for condition, seq in conditions.items():
    conditions[condition] = ['Intro'] + seq

add_end_region = True
autocaps = True

def make_definite(s):
    words = s.split()
    words[0] = "the"
    return " ".join(words)

def expand_items(df):
    df['S'] = "'s"
    df['the'] = "the"
    df['of'] = "of"
    df['Indef Possessor'] = df['Possessor']
    df['Def Possessor'] = df['Indef Possessor'].map(make_definite)
    output_df = pd.DataFrame(rows(df))
    output_df.columns = ['sent_index', 'word_index', 'word', 'region', 'condition']
    return output_df

def rows(df):
    for condition in conditions:
        for sent_index, row in df.iterrows():
            word_index = 0
            for region in conditions[condition]:
                for word in row[region].split():
                    if autocaps and word_index == 0:
                        word = word.title()
                    yield sent_index, word_index, word, region, condition
                    word_index += 1
            if add_end_region:
                yield sent_index, word_index + 1, ".", "End", condition
                yield sent_index, word_index + 2, "<eos>", "End", condition
            
def main(filename):
    input_df = pd.read_excel(filename)
    output_df = expand_items(input_df)
    try:
        os.mkdir("tests")
    except FileExistsError:
        pass
    output_df.to_csv("tests/items.tsv", sep="\t")

if __name__ == "__main__":
    main(*sys.argv[1:])

