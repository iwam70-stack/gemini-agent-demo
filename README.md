# gemini-agent-demo

## 使い方

`src/file_list.py` は、指定したディレクトリ内のファイル名を一覧表示する簡易スクリプトです。

### 実行方法

```bash
python src/file_list.py [directory]
```

- `directory` を省略した場合は、現在の作業ディレクトリを対象にします。
- 例:

```bash
python src/file_list.py /tmp
```

上記を実行すると `/tmp` 配下のファイル名が1行ずつ表示されます。
