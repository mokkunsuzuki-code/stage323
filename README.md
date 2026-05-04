# Stage323: YubiKey Signed Audit History

Turn any audit log into a **verifiable, issuer-backed proof**.

Stop trusting logs. Start verifying accountability.

---

## 概要

監査ログを「検証可能な責任付き証明」に変換する。

Stage322では監査履歴が作成されました。  
Stage323では、その履歴に **GPG + YubiKeyによる署名** を追加し、

> **「誰がこの履歴に責任を持つか」**

を暗号的に固定します。

---

## なぜ必要か

従来の監査ログには問題があります：

- 改ざんされる可能性がある  
- 誰が責任を持つか不明  
- 外部から検証できない  

---

## これができること

- 監査履歴の改ざん検知  
- 発行者の特定（署名）  
- 第三者による検証  
- YubiKeyによる鍵保護  

---

## コア構造

history.json
  ↓
history.json.sig
  ↓
public-key.asc
  ↓
third-party verification

---

## ファイル構成

- docs/proofs/history.json  
- docs/proofs/history.json.sig  
- docs/proofs/public-key.asc  
- verify_signature.sh  

---

## 検証方法

```bash
./verify_signature.sh

または：

gpg --import docs/proofs/public-key.asc
gpg --verify docs/proofs/history.json.sig docs/proofs/history.json
これが証明すること
監査履歴が存在する
監査履歴が改ざんされていない
特定の発行者によって署名されている
発行者の鍵がYubiKeyで保護されている
本質

履歴がある（Stage322）
↓
誰が責任を持つかが証明される（Stage323）

Who Needs This?
セキュリティチーム
コンプライアンス対応企業
AI出力の証明が必要なケース
改ざん不可能なログが必要な場面
Live Demo

https://mokkunsuzuki-code.github.io/stage323/

Upgrade

署名付き履歴の管理・API化・組織承認が必要ですか？

👉 REMEDA Pro（予定）

Security Policy

公開しないもの：

秘密鍵
coreロジック
.env
keys/
License

MIT License

Copyright (c) 2025 Motohiro Suzuki
