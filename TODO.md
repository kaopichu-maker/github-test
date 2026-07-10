# TODO

## Backlog

- [ ] Define the project purpose in more detail.
- [ ] Add source materials to `materials/`.
- [ ] Add reusable assets to `assets/`.
- [ ] Save final deliverables to `outputs/`.
- [ ] Update this list as tasks are clarified.

## Next Session

- [x] Restart Codex Desktop so Git, GitHub CLI, and Node.js PATH changes take effect.
- [ ] Confirm the GitHub plugin installation in Codex Desktop.
- [x] Run `gh auth login` to sign in to GitHub CLI.
- [ ] Re-check `git --version`, `gh --version`, `node --version`, and `uv --version`.
- [x] Initialize Git for this project if version control is needed.
- [x] Continue with Codex lazy guide #02 to connect GitHub.

## Open Items

- [ ] GitHub plugin is not confirmed as enabled yet.
- [x] GitHub CLI is installed and logged in as kaopichu-maker.
- [x] This folder is now a Git repository on branch main.
- [ ] Local files are not committed yet.
- [ ] Remote origin points to existing repo https://github.com/kaopichu-maker/github-test.git; push strategy still needs confirmation because the remote already has a commit.

## 2026-07-06 Closeout

- [x] 完成 GitHub CLI 登入：`kaopichu-maker`
- [x] 設定 Git 全域提交資訊：
  - `user.name`: `kaopichu-maker`
  - `user.email`: `300374369+kaopichu-maker@users.noreply.github.com`
- [x] 建立並推送 GitHub 測試 repo：`https://github.com/kaopichu-maker/github-test`
- [x] 啟用並驗證 GitHub Pages：`https://kaopichu-maker.github.io/github-test/`
- [x] 依使用者決定保留 `github-test` 測試 repo。

## Next Session

- 若要上線新的教材或網頁，可直接建立 repo、推送內容並啟用 GitHub Pages。
- 目前工作區 `G:\我的雲端硬碟\2026 Codex 初始化 2026.07` 已初始化為 Git repo，並連到 `github-test`；下一次可先決定是否提交並推送，或改建立專用 repo。

## 2026-07-08 Closeout

- [x] 確認 GitHub CLI 已登入帳號：kaopichu-maker
- [x] 將目前工作區初始化為 Git repo，分支為 main。
- [x] 設定遠端 origin：https://github.com/kaopichu-maker/github-test.git
- [ ] 尚未提交本機檔案。
- [ ] 尚未推送本工作區內容到 GitHub。
- [ ] 推送前需先決定是否沿用 github-test，或為此工作區建立新的 GitHub repo。

## 2026-07-08 Obsidian Closeout

- [x] 安裝 Obsidian 1.12.7。
- [x] 安裝全域 mcpvault：`C:\Users\kaopi\AppData\Roaming\npm\mcpvault.cmd`
- [x] 建立 Obsidian vault：`G:\我的雲端硬碟\secondbrain`
- [x] 建立 vault 資料夾：`教學素材`、`影片筆記`、`每日筆記`、`Templates`
- [x] 建立基礎筆記與模板：`CLAUDE.md`、`index.md`、`test-note.md`、`secondbrain-start.md`、`Templates/daily-note-template.md`、`Templates/teaching-reflection-template.md`
- [x] 寫入 Claude / Codex MCP 設定：`.claude/settings.local.json`、`.mcp.json`、`C:\Users\kaopi\.claude\settings.json`、`C:\Users\kaopi\.codex\config.toml`
- [x] 重啟 Codex Desktop，確認 `mcp__obsidian__` 工具是否載入。
- [x] 在 Obsidian app 中確認 `secondbrain` vault 已正確登錄並開啟。
- [ ] 補填 `CLAUDE.md` 中的科目、年級與個人偏好。
- [ ] mcpvault 中文搜尋仍需後續觀察；目前建議檔名與 tags 用英文，內容可用中文。

## 2026-07-08 MCPVault / Obsidian Fix Closeout

- [x] 修正 Obsidian app 金庫登錄：由 `G:\我的雲端硬碟` 改為 `G:\我的雲端硬碟\secondbrain`。
- [x] 將誤建在 `G:\我的雲端硬碟\.obsidian` 的設定資料夾移到 `G:\我的雲端硬碟\secondbrain\.obsidian`。
- [x] 備份 Obsidian 登錄檔：`C:\Users\kaopi\AppData\Roaming\obsidian\obsidian.json.bak-20260708-secondbrain`。
- [x] 重啟 Codex 後確認 `mcp__obsidian__` 工具已載入。
- [x] 透過 MCP 成功讀取 `index.md`，並確認金庫統計為 6 篇筆記、4 個資料夾。
- [ ] 本工作區檔案仍未提交。
- [ ] 本工作區內容仍未推送到 GitHub。




## 2026-07-09 第二大腦 #04 / Web Clipper Closeout

- [x] 確認 Obsidian app 已安裝：`Obsidian.Obsidian 1.12.7`。
- [x] 確認全域 `@bitbonsai/mcpvault@0.12.1` 已安裝，且 Codex MCP 可讀取 `secondbrain` vault。
- [x] 依 `04-第二大腦設定指南.md` 補齊第二大腦結構：`Clippings/`、`知識庫/`、`創作庫/`、`每日筆記/`、`Templates/`。
- [x] 依使用者資料更新 `CLAUDE.md`：國小六年級、國語、數學、社會、七個習慣、綜合、閱讀；偏好繁體中文、簡潔白話、附教學建議。
- [x] 建立模板：`Templates/每日筆記.md`、`Templates/週計畫.md`、`Templates/知識庫頁面.md`。
- [x] 建立 `知識庫/index.md`、`知識庫/log.md`、`歡迎來到你的第二大腦.md`。
- [x] 建立每週日 09:17 的知識重整排程：`weekly-knowledge-review`。
- [x] 驗證 Obsidian Web Clipper 的 `Default` 模板 path 為 `Clippings`。
- [ ] Chrome 曾顯示 Web Clipper 設定頁 `ERR_BLOCKED_BY_CLIENT`，但底層 extension storage 已確認路徑正確；日後若要改 UI 設定需再處理 Chrome 擴充功能頁面封鎖問題。
- [ ] 本工作區檔案仍未提交。
- [ ] 本工作區內容仍未推送到 GitHub。
