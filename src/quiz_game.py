#!/usr/bin/env python3
"""四則演算のクイズを出題し、正解までの最初の回答時間を表示するゲーム."""

from __future__ import annotations

import random
import time


def generate_question() -> tuple[int, str, int, int]:
    """2桁以上の四則演算問題を生成する。"""
    left = random.randint(10, 99)
    right = random.randint(10, 99)
    operator = random.choice(["+", "-", "*", "/"])

    if operator == "+":
        answer = left + right
    elif operator == "-":
        answer = left - right
    elif operator == "*":
        answer = left * right
    else:
        answer = left // right
        if left % right != 0:
            left = right * answer + left % right
        right = answer
        answer = left // right

    return left, operator, right, answer


def run_quiz() -> None:
    """問題を出題し、最初の回答から正解までの時間を表示する。"""
    start = time.monotonic()
    left, operator, right, answer = generate_question()
    print(f"{left} {operator} {right} = ?")

    user_answer = input("答えを入力してください: ")
    elapsed = int(time.monotonic() - start)

    if int(user_answer) == answer:
        print(f"正解です! 最初の回答までの経過時間: {elapsed}秒")
    else:
        print(f"不正解です。正解は {answer} でした。")


if __name__ == "__main__":
    run_quiz()
