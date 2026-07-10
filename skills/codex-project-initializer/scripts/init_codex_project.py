import argparse
from datetime import date
from pathlib import Path


def write_if_missing(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.write_text(content, encoding="utf-8", newline="\n")
    return True


def zh_templates(purpose: str) -> dict[str, str]:
    today = date.today().isoformat()
    return {
        "README.md": f"""# {purpose}

這個專案用來：{purpose}

## 專案用途

- 整理專案目標與內容
- 保存原始資料、素材與輸出成果
- 讓 Codex 後續能依照專案脈絡協助製作、修改與檢查

## 資料夾結構

- `materials/`：原始資料、參考內容、課程筆記、文字草稿
- `assets/`：圖片、截圖、圖示、視覺素材
- `outputs/`：成品、匯出檔、預覽圖與交付成果

## 下一步

確認內容大綱、目標讀者與第一個要製作的成果。
""",
        "AGENTS.md": f"""# AGENTS.md - 專案工作指引

本檔案是此專案的專用工作指引，不是全域規則。

## 專案目標

{purpose}

## 工作原則

- 優先依照使用者的明確指示執行。
- 修改檔案前先讀取現有內容，避免覆蓋使用者新增的資料。
- 只加入與本專案用途相關的內容。
- 不套用與本專案無關的全域規則或通用範本。
- 完成後說明已完成、已確認與尚未確認的事項。

## 檔案放置規則

- 原始資料與參考內容放在 `materials/`。
- 圖片、截圖、圖示與視覺素材放在 `assets/`。
- 成品、匯出檔與交付成果放在 `outputs/`。
- 專案進度更新寫入 `PROGRESS.md`。
- 待辦事項更新寫入 `TODO.md`。
""",
        "TODO.md": """# TODO

## 待辦

- [ ] 確認專案目標與目標讀者
- [ ] 整理第一版內容大綱
- [ ] 收集或建立需要的素材
- [ ] 製作第一版成果
- [ ] 檢查成果並記錄需要修改的地方

## 可延後

- [ ] 補充進階內容
- [ ] 整理最終交付版本
""",
        "PROGRESS.md": f"""# PROGRESS

## {today}

### 已完成

- 初始化 Codex 專案結構
- 建立 `README.md`
- 建立專案專用 `AGENTS.md`
- 建立 `TODO.md`
- 建立 `PROGRESS.md`
- 建立 `materials/`、`assets/`、`outputs/` 資料夾

### 目前狀態

專案已完成基本初始化，尚未開始製作實際成果。

### 下一步

確認專案內容大綱與第一個要製作的成果。
""",
    }


def en_templates(purpose: str) -> dict[str, str]:
    today = date.today().isoformat()
    return {
        "README.md": f"""# {purpose}

This project is for: {purpose}

## Structure

- `materials/`: source material, notes, references, drafts
- `assets/`: images, screenshots, icons, visual assets
- `outputs/`: final artifacts, exports, previews, deliverables

## Next Step

Confirm the outline, audience, and first deliverable.
""",
        "AGENTS.md": f"""# AGENTS.md - Project Instructions

This file is project-specific guidance, not global guidance.

## Project Goal

{purpose}

## Working Rules

- Follow explicit user instructions first.
- Read existing files before editing.
- Add only content relevant to this project.
- Do not apply unrelated global rule sets or generic templates.
- Report what changed, what was verified, and what remains uncertain.

## File Placement

- Put source materials in `materials/`.
- Put images and visual assets in `assets/`.
- Put deliverables and exports in `outputs/`.
- Track progress in `PROGRESS.md`.
- Track tasks in `TODO.md`.
""",
        "TODO.md": """# TODO

## Tasks

- [ ] Confirm project goal and audience
- [ ] Draft the first outline
- [ ] Collect or create required assets
- [ ] Create the first deliverable
- [ ] Review and record needed changes
""",
        "PROGRESS.md": f"""# PROGRESS

## {today}

### Completed

- Initialized Codex project structure
- Created `README.md`
- Created project-specific `AGENTS.md`
- Created `TODO.md`
- Created `PROGRESS.md`
- Created `materials/`, `assets/`, and `outputs/`

### Current Status

The project is initialized. No deliverable has been created yet.

### Next Step

Confirm the outline and first deliverable.
""",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Initialize a Codex-friendly project workspace.")
    parser.add_argument("--root", default=".", help="Target project root.")
    parser.add_argument("--purpose", required=True, help="Project purpose or title.")
    parser.add_argument("--language", choices=["zh-Hant", "en"], default="zh-Hant")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)

    for dirname in ["materials", "assets", "outputs"]:
        folder = root / dirname
        folder.mkdir(exist_ok=True)
        write_if_missing(folder / ".gitkeep", "\n")

    templates = zh_templates(args.purpose) if args.language == "zh-Hant" else en_templates(args.purpose)
    created = []
    skipped = []
    for filename, content in templates.items():
        target = root / filename
        if write_if_missing(target, content):
            created.append(filename)
        else:
            skipped.append(filename)

    print("Created: " + (", ".join(created) if created else "none"))
    print("Skipped existing: " + (", ".join(skipped) if skipped else "none"))
    print(f"Root: {root}")


if __name__ == "__main__":
    main()
