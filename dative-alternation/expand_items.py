import os
import sys
import itertools

import pandas as pd

conditions = {
    'do_theme-short_theme-indefinite_recip-short_recip-indefinite': ['Indef Recipient', 'Indef Theme'],
    'do_theme-short_theme-definite_recip-short_recip-indefinite': ['Def Recipient', 'Indef Theme'],
    'do_theme-short_theme-indefinite_recip-short_recip-definite': ['Indef Recipient', 'Def Theme'],
    'do_theme-short_theme-definite_recip-short_recip-definite': ['Def Recipient', 'Def Theme'],
    'do_theme-long_theme-indefinite_recip-short_recip-indefinite': ['Indef Recipient', 'Indef Theme', 'Theme Modifier'],
    'do_theme-long_theme-definite_recip-short_recip-indefinite': ['Def Recipient', 'Indef Theme', 'Theme Modifier'],
    'do_theme-long_theme-indefinite_recip-short_recip-definite': ['Indef Recipient', 'Def Theme', 'Theme Modifier'],
    'do_theme-long_theme-definite_recip-short_recip-definite': ['Def Recipient', 'Def Theme','Theme Modifier'], 
    'do_theme-short_theme-indefinite_recip-long_recip-indefinite': ['Indef Recipient', 'Recipient Modifier', 'Indef Theme'],
    'do_theme-short_theme-definite_recip-long_recip-indefinite': ['Def Recipient', 'Recipient Modifier', 'Indef Theme'],
    'do_theme-short_theme-indefinite_recip-long_recip-definite': ['Indef Recipient', 'Recipient Modifier', 'Def Theme'],
    'do_theme-short_theme-definite_recip-long_recip-definite': ['Def Recipient', 'Recipient Modifier', 'Def Theme'],
    'do_theme-long_theme-indefinite_recip-long_recip-indefinite': ['Indef Recipient', 'Recipient Modifier', 'Indef Theme', 'Theme Modifier'],
    'do_theme-long_theme-definite_recip-long_recip-indefinite': ['Def Recipient', 'Recipient Modifier', 'Indef Theme', 'Theme Modifier'],
    'do_theme-long_theme-indefinite_recip-long_recip-definite': ['Indef Recipient', 'Recipient Modifier', 'Def Theme', 'Theme Modifier'],
    'do_theme-long_theme-definite_recip-long_recip-definite': ['Def Recipient', 'Recipient Modifier', 'Def Theme', 'Theme Modifier'],

    'po_theme-short_theme-indefinite_recip-short_recip-indefinite': ['Indef Theme', 'To', 'Indef Recipient'],
    'po_theme-short_theme-definite_recip-short_recip-indefinite': ['Indef Theme', 'To', 'Def Recipient'],
    'po_theme-short_theme-indefinite_recip-short_recip-definite': ['Def Theme', 'To', 'Indef Recipient'],
    'po_theme-short_theme-definite_recip-short_recip-definite': ['Def Theme', 'To', 'Def Recipient'],
    
    'po_theme-long_theme-indefinite_recip-short_recip-indefinite': ['Indef Theme', 'Theme Modifier', 'To', 'Indef Recipient'],
    'po_theme-long_theme-definite_recip-short_recip-indefinite': ['Indef Theme', 'Theme Modifier', 'To', 'Def Recipient'],
    'po_theme-long_theme-indefinite_recip-short_recip-definite': ['Def Theme', 'Theme Modifier', 'To', 'Indef Recipient'],
    'po_theme-long_theme-definite_recip-short_recip-definite': ['Def Theme','Theme Modifier', 'To', 'Def Recipient'],
    
    'po_theme-short_theme-indefinite_recip-long_recip-indefinite': ['Indef Theme', 'To', 'Indef Recipient', 'Recipient Modifier', ],
    'po_theme-short_theme-definite_recip-long_recip-indefinite': ['Indef Theme', 'To', 'Def Recipient', 'Recipient Modifier', ],
    'po_theme-short_theme-indefinite_recip-long_recip-definite': ['Def Theme', 'To', 'Indef Recipient', 'Recipient Modifier', ],
    'po_theme-short_theme-definite_recip-long_recip-definite': ['Def Theme', 'To', 'Def Recipient', 'Recipient Modifier', ],
    
    'po_theme-long_theme-indefinite_recip-long_recip-indefinite': ['Indef Theme', 'Theme Modifier', 'To', 'Indef Recipient', 'Recipient Modifier', ],
    'po_theme-long_theme-definite_recip-long_recip-indefinite': ['Indef Theme', 'Theme Modifier', 'To', 'Def Recipient', 'Recipient Modifier', ],
    'po_theme-long_theme-indefinite_recip-long_recip-definite': ['Def Theme', 'Theme Modifier', 'To', 'Indef Recipient', 'Recipient Modifier', ],
    'po_theme-long_theme-definite_recip-long_recip-definite': ['Def Theme', 'Theme Modifier', 'To', 'Def Recipient', 'Recipient Modifier', ],    
}

for condition in conditions:
    conditions[condition] = ['Subject', 'Verb'] + conditions[condition]

end_condition_included = False
autocaps = True

def make_definite(s):
    words = s.split()
    words[0] = "the"
    return " ".join(words)

def expand_items(df):
    df['To'] = "to"
    df['Indef Theme'] = df['Theme']
    df['Indef Recipient'] = df['Recipient']
    df['Def Theme'] = df['Indef Theme'].map(make_definite)
    df['Def Recipient'] = df['Indef Recipient'].map(make_definite)
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
            if not end_condition_included:
                yield sent_index, word_index + 1, ".", "End", condition
                yield sent_index, word_index + 2, "<eos>", "End", condition

def main(filename:
    input_df = pd.read_excel(filename)
    output_df = expand_items(input_df)
    try:
        os.mkdir("tests")
    except FileExistsError:
        pass

if __name__ == "__main__":
    main(*sys.argv[1:])

