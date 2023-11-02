import nltk
nltk.download("punkt")
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def summarize(text, language="english", sentences_count=5):
    parser = PlaintextParser.from_string(text, Tokenizer(language))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count)
    return ' '.join([str(sentence) for sentence in summary])

if __name__ == "__main__":
    text = "<input your text>"
    summary = summarize(text)
    print(summary)

file = open("<FILE PATH>","w")
file.write(summary)