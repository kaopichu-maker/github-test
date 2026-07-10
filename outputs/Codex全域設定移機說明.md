# Codex 全域設定與 Skills 移機說明

## 這個壓縮包包含什麼

這份全域搬家包包含使用者層級的 Codex 可移植設定：

- `.codex/AGENTS.md`
- `.codex/config.toml`
- `.codex/keybindings.json`
- `.codex/skills/`
- `.codex/rules/`

## 這個壓縮包刻意不包含什麼

為了避免把登入狀態、機器狀態、快取或紀錄搬到另一台電腦，壓縮包不包含：

- `.codex/auth.json`
- `.codex/sessions/`
- `.codex/logs_*.sqlite`
- `.codex/state_*.sqlite`
- `.codex/cache/`
- `.codex/.sandbox-secrets/`
- `.codex/tmp/`
- `.codex/.tmp/`

## 到另一台電腦的建議順序

1. 先安裝並啟動 Codex。
2. 讓 Codex 在新電腦建立自己的使用者層級 `.codex` 資料夾。
3. 關閉 Codex。
4. 解壓縮這份全域搬家包。
5. 將壓縮包內的 `.codex/AGENTS.md`、`.codex/config.toml`、`.codex/keybindings.json`、`.codex/skills/`、`.codex/rules/` 複製到新電腦的使用者層級 `.codex` 資料夾。
6. 重新開啟 Codex。
7. 在新電腦重新登入 Codex，並重新安裝需要登入授權的 plugins 或 connectors。

## 重要提醒

不要直接覆蓋新電腦的 `auth.json`、sessions、logs、state sqlite、cache 或 sandbox secrets。這些通常和登入、機器、執行狀態或隱私資料有關，不適合跨電腦搬移。
