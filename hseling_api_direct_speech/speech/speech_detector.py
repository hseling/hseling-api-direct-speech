import re
from .step import PipelineStep


class SpeechDetector(PipelineStep):
    def __init__(self, path):
        super().__init__()
        self.rule_df = self.read_csv(path, ';')

    def annotate(self, text):
        for left, speech, right in self.rule_df:
            text = self.__find_speech(left, speech, right, text)
            text = re.sub('(<speech>)+', '<speech>', text)
            text = re.sub('(</speech>)+', '</speech>', text)
        return text

    def __compute_regex(self, left_context, speech, right_context):
        try:
            regex = re.compile("(" + left_context + ")" + "(" + speech + ")" +
                               "(" + right_context + ")",
                               flags=re.MULTILINE)
            return regex
        except Exception:
            print("EXCEPTION IN REG EXP:", left_context, speech, right_context)
            return "EXCEPTION IN REG EXP"

    def __find_speech(self, left_context, speech, right_context, text):
        rule = self.__compute_regex(left_context, speech, right_context)
        text = re.sub(rule, r"\g<1><speech>\g<2></speech>\g<3>", text)
        return text
