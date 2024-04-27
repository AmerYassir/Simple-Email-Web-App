from spam_detector_ai.prediction.predict import VotingSpamDetector
import nltk
#downlaoding necessary word sets for preprocessing purpuses
nltk.download('wordnet')
nltk.download('stopwords')
# Create the spam detector

class spam_detector():
    def __init__(self) -> None:
        self.spam_detector = VotingSpamDetector()
    def test_message(self,email_body):
        # Check if a message is spam
        is_spam = self.spam_detector.is_spam(email_body)
        return is_spam