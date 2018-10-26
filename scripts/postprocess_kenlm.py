#This=396580 2 -1.9561708        is=5095350 3 -0.6661906 a=166085 4 -0.75032955  test=1104044 5 -2.6113853       .=799379 5 -1.6290084   </s>=2521587 5 -0.04999798      Total: -7.6630826 OOV: 0
#I=3032606 2 -1.8025744  like=1788818 3 -2.1346579       tests=1122157 2 -5.7637467      .=799379 2 -1.575114    </s>=2521587 3 -0.034977615     Total: -11.311071 OOV: 0
#Perplexity including OOVs:      53.07904378756336
#Perplexity excluding OOVs:      53.07904378756336
#OOVs:   0
#Tokens: 11
import sys
import math

def words_and_surprisals(line):
    *tokens, final = line.split("\t")
    assert final.startswith("Total:")
    num_unks = 0
    for token in tokens:
        word, number, logprob = token.split()
        wordform, index = word.split("=")
        if int(index) == 0:
            wordform = "<UNK>"
            num_unks += 1
        # Kenlm log probs are in base 10 so convert to base 2        
        logprob = float(logprob) / math.log(2, 10)
        yield wordform, -logprob
    total, total_score, oov, num_oov = final.split()
    assert int(num_oov) == num_unks, (num_oov, num_unks)

def process_lines(lines):
    for line in lines:
        if line.startswith("Perplexity including"):
            break
        yield from words_and_surprisals(line)

def main():
    results = process_lines(map(str.strip, sys.stdin))
    for wordform, surprisal in results:
        print(wordform, surprisal, sep="\t")

if __name__ == '__main__':
    main()
    
    

