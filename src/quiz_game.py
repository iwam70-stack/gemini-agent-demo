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
        divisor = random.randint(10, 99)
        quotient = random.randint(10, 99)
        answer = quotient
        left = divisor * quotient
        right = divisor

    return left, operator, right, answer


def run_quiz() -> None:
    """問題を出題し、最初の回答から正解までの時間を表示する。"""
    start = time.monotonic()
    left, operator, right, answer = generate_question()
    print(f"{left} {operator} {right} = ?")

    while True:
        try:
            user_answer = input("答えを入力してください: ")
            if user_answer == "":
                raise ValueError("入力が空です")
            value = int(user_answer)
        except (ValueError, TypeError):
            print("入力が不正です。整数を入力してください。")
            continue

        elapsed = int(time.monotonic() - start)
        if value == answer:
            print(f"正解です! 最初の回答までの経過時間: {elapsed}秒")
            return

        print(f"不正解です。もう一度入力してください。")
        # 失敗した場合も引き続き問題を再入力させる
        print(f"{left} {operator} {right} = ?")


if __name__ == "__main__":
    run_quiz()
