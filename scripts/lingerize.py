import sys
import itertools
import operator

import pandas as pd

def humanize_punctuation(s):
    return s.replace(" .", ".").replace(" ,", ",").replace(" ?", "?").replace(" !", "!").replace(" 's", "'s")

def humanize(df):
    result = (
        df
        .loc[lambda x: x['word'] != '<eos>']
        .groupby(['sent_index', 'condition'])
        .agg({'word': " ".join})
        .reset_index()
    )
    result['word'] = result['word'].map(humanize_punctuation)
    return result

flat = itertools.chain.from_iterable

def uniq(iterable):
    "List unique elements, preserving order. Remember only the element just seen."
    return map(next, map(operator.itemgetter(1), itertools.groupby(iterable)))

def the_unique(xs):
    ys = list(uniq(xs))
    assert len(ys) == 1
    return ys[0]

def write_linger(df, experiment_name):
    def make_linger_group(df):
        index = the_unique(df['sent_index'])
        def gen():
            for i, row in df.iterrows():
                yield " ".join([experiment_name, str(index), row['condition']])
                yield row['word']
                yield "? "
        return pd.Series({'text': "\n".join(gen())})

    items = (
        df
        .groupby(['sent_index'])
        .apply(make_linger_group)
        .reset_index()
    )
    return items['text']

def main(filename, experiment_name):
    df = pd.read_csv(filename, sep="\t")
    hdf = humanize(df)
    lines = write_linger(hdf, experiment_name)
    for line in lines:
        print(line, end="\n\n")

if __name__ == '__main__':
    main(*sys.argv[1:])
    
