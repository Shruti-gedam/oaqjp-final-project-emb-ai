"""Unit tests for the EmotionDetection package."""

import json
import unittest
from unittest.mock import Mock, patch

from EmotionDetection import emotion_detector


def response_for(dominant):
    """Build a Watson-shaped response where one emotion is highest."""
    scores = {
        "anger": 0.1,
        "disgust": 0.1,
        "fear": 0.1,
        "joy": 0.1,
        "sadness": 0.1,
    }
    scores[dominant] = 0.9
    return Mock(
        text=json.dumps(
            {"emotionPredictions": [{"emotion": scores}]}
        ),
        status_code=200,
    )


class EmotionDetectorTests(unittest.TestCase):
    """Check dominant-emotion formatting for every emotion."""

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_anger(self, post):
        post.return_value = response_for("anger")
        self.assertEqual(emotion_detector("sample")["dominant_emotion"], "anger")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_disgust(self, post):
        post.return_value = response_for("disgust")
        self.assertEqual(emotion_detector("sample")["dominant_emotion"], "disgust")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_fear(self, post):
        post.return_value = response_for("fear")
        self.assertEqual(emotion_detector("sample")["dominant_emotion"], "fear")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_joy(self, post):
        post.return_value = response_for("joy")
        self.assertEqual(emotion_detector("sample")["dominant_emotion"], "joy")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_sadness(self, post):
        post.return_value = response_for("sadness")
        self.assertEqual(emotion_detector("sample")["dominant_emotion"], "sadness")


if __name__ == "__main__":
    unittest.main()
