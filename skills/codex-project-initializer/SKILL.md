---
name: codex-project-initializer
description: Initialize a Codex-friendly project workspace with project-specific README.md, AGENTS.md, TODO.md, PROGRESS.md, and standard folders such as materials, assets, and outputs. Use when the user asks to initialize a project, set up a Codex project, create project scaffolding, prepare a teaching/content/web project workspace, or make a reusable project structure without applying global AGENTS rules.
---

# Codex Project Initializer

Create a small, project-specific workspace scaffold that helps Codex and the user track purpose, rules, tasks, progress, source materials, assets, and outputs.

## Workflow

1. Inspect the target folder before writing.
2. Identify the project purpose from the user request. If the purpose is missing, ask one concise question before creating content.
3. Define success for initialization as:
   - `README.md` exists and explains the project purpose, audience, structure, and next step.
   - `AGENTS.md` exists and contains project-specific guidance only.
   - `TODO.md` exists and lists actionable next steps.
   - `PROGRESS.md` exists and records initialization status with the current date.
   - `materials/`, `assets/`, and `outputs/` exist.
4. Preserve user work. If any target file already exists, read it first and update surgically instead of overwriting.
5. Keep initialization lightweight. Do not add frameworks, package managers, git repositories, build systems, or deployment config unless the user asks.
6. Classify project type from local evidence before suggesting extras:
   - Existing `.git/`: respect the current Git repository and do not reinitialize it.
   - Explicit user request for Git, repo, GitHub, version control, commit, or push: include Git setup or next Git steps.
   - Code project evidence such as `package.json`, `pyproject.toml`, `requirements.txt`, `Cargo.toml`, source folders, or tests: suggest Git if missing, but ask before running `git init`.
   - Asset/document project evidence such as images, videos, `.docx`, `.pptx`, `.pdf`, or teaching materials: do not add Git by default; mention it as an optional next step only when useful.
7. Apply an impact gate:
   - Low-impact actions can be done directly: create or surgically update `README.md`, `AGENTS.md`, `TODO.md`, `PROGRESS.md`; create `materials/`, `assets/`, and `outputs/`.
   - Medium-impact actions require explicit confirmation unless already requested: move existing files, reorganize folders, initialize Git, add `.gitignore`, or convert outputs.
   - High-impact actions require explicit confirmation: delete files, overwrite substantial existing content, install packages, create frameworks, connect remotes, push to GitHub, or change deployment config.
8. Use Traditional Chinese for Taiwan education or user-facing teaching projects unless the user specifies another language.

## AGENTS.md Rules

- Treat `AGENTS.md` as project-level instructions, not global instructions.
- Do not copy generic global rule sets unless the user explicitly asks for them.
- Include only durable guidance that helps future work in this project.
- Mention the project root or scope when useful.
- Include file placement rules for `materials/`, `assets/`, and `outputs/`.

## Optional Script

For a fresh or lightly populated folder, use `scripts/init_codex_project.py` to generate baseline files and folders. Read or inspect existing files first when the folder is not empty.

Example:

```powershell
python scripts/init_codex_project.py --root "C:\path\to\project" --purpose "做一個教學生使用 Codex 的網頁" --language zh-Hant
```

After running the script, review the generated files and adjust wording to the user's specific project.

## Completion Report

Report:

- What changed
- What was verified
- What remains undecided or not run
