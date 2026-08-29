import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from src.quiz_game import generate_question, run_quiz


class QuizGameTests(unittest.TestCase):
    def test_generate_question_uses_two_digit_or_more_numbers(self):
        question = generate_question()
        self.assertGreaterEqual(question[0], 10)
        self.assertGreaterEqual(question[2], 10)
        self.assertIn(question[1], ["+", "-", "*", "/"])

    def test_generate_question_for_division_is_naturally_valid(self):
        for _ in range(200):
            question = generate_question()
            if question[1] == "/":
                self.assertEqual(question[0], question[2] * question[3])
                self.assertGreaterEqual(question[2], 10)
                break
        else:
            self.fail("Division question was not generated")

    def test_run_quiz_handles_invalid_input_and_reports_elapsed_time(self):
        question = (12, "+", 13, 25)

        with patch("src.quiz_game.generate_question", return_value=question), \
             patch("src.quiz_game.time.monotonic", side_effect=[100.0, 104.2]), \
             patch("builtins.input", side_effect=["", "25"]):
            stdout = io.StringIO()
            with redirect_stdout(stdout):
                run_quiz()

        output = stdout.getvalue()
        self.assertIn("入力が不正", output)
        self.assertIn("経過時間", output)
        self.assertIn("4秒", output)


if __name__ == "__main__":
    unittest.main()
