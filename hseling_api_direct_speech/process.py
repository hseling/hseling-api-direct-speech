from .speech.quotes_processing import QuotesAdapter
from .speech.speech_detector import SpeechDetector
from .speech.file_reader import FileReader
from .speech.sentiment_detector import SentimentDetector
from .speech.verb_tagger import VerbTagger
from .speech.pipeline import Pipeline
from .speech.said_comment_tagger import SaidCommentTagger
from bs4 import BeautifulSoup


def read_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()


def process_data(data):
    file_id = None
    result = ""
    for file_id, contents in data.items():
        if isinstance(contents, bytes):
            text = contents.decode('utf-8')
        else:
            text = contents

        reader = FileReader()
        quotes_adapter = QuotesAdapter("csv_files/quotes.csv")
        speech_detector = SpeechDetector("csv_files/speech.csv")
        said_comment_tagger = SaidCommentTagger()
        verb_tagger = VerbTagger("csv_files/verbs.csv")
        sentiment_detector = SentimentDetector()
        pipeline = Pipeline(reader, quotes_adapter, speech_detector, said_comment_tagger, verb_tagger,
                            sentiment_detector)
        result = pipeline.apply_to(text)
        file_id = file_id
    if result:
        yield file_id, result

