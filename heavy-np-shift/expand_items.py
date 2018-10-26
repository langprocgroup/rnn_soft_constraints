import os
import sys

import pandas as pd

conditions = {
    'short_np_unshifted': ['Subject', 'NP Verb', 'Short NP', 'PP'],
    'short_np_shifted': ['Subject', 'NP Verb', 'PP', 'Short NP'],
    'short_nps_unshifted': ['Subject', 'NP/S Verb', 'Short NP', 'PP'],
    'short_nps_shifted': ['Subject', 'NP/S Verb', 'PP', 'Short NP'],
    'long_np_unshifted': ['Subject', 'NP Verb', 'Long NP', 'PP'],
    'long_np_shifted': ['Subject', 'NP Verb', 'PP', 'Long NP'],
    'long_nps_unshifted': ['Subject', 'NP/S Verb', 'Long NP', 'PP'],
    'long_nps_shifted': ['Subject', 'NP/S Verb', 'PP', 'Long NP'],
}

add_end_region = True
autocaps = True

def expand_items(df):
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

