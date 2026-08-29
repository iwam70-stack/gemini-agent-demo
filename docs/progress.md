# 作業進捗

## 現在の状態

- `design.md` の指示に基づくクイズゲームを実装済み
- `src/quiz_game.py` と `test/test_quiz_game.py` を追加済み
- 除算ロジックと入力エラー処理の修正を反映済み
- `docs/` 配下の進捗・判断・要件記録を更新済み

## 完了した作業

- `src/file_list.py` の実装
- `src/quiz_game.py` の実装
- `src/quiz_game.py` の除算ロジック修正
- `input()` の空文字・非数値例外処理追加
- 不正解時の再入力ループ追加
- `test/test_quiz_game.py` の拡張
- `docs/decisions.md` への判断追加

## 作業中

- なし

## 未完了

- なし

## テスト状況

- 実行したテスト: `python -m unittest discover -s test -q`
- 結果: 成功（5 tests, OK）

## 次に行う作業

1. 最終確認を行う
2. git add / commit / push を実施する

## 注意事項

- `design.md` は固定の指示書として扱い、内容変更は原則禁止
- 実際の変更履歴は `docs/decisions.md` に記録する
