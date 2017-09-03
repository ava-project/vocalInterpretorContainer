from watson_developer_cloud import SpeechToTextV1


class STT_Engine():

    def __init__(self):
        self.stt = SpeechToTextV1(
            username = 'ed8e6084-ebe7-4570-a387-be01bcefcad5',
            password = 'ksiqNlaLyhaX',
            x_watson_learning_opt_out=False
        )

    def recognize(self, stream):
        return self.stt.recognize(
            stream, content_type='audio/wav', timestamps=True,
            word_confidence=True)
