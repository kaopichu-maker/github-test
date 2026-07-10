# Global Project Initializer

Use this skill when the user asks to initialize a project, prepare a repository for Codex/AI-agent work, create or update project-level agent instructions, or set up a lightweight project baseline across different workspaces.

This skill is intentionally conservative. It should help define the project working rules, verify the current state, and make the smallest useful initialization changes without imposing a framework, architecture, or workflow the user did not ask for.

## Goals

- Clarify the project purpose, constraints, and success criteria before changing files.
- Inspect the current workspace before deciding what to create or modify.
- Create or update the project baseline files: `README.md`, `AGENTS.md`, `TODO.md`, and `PROGRESS.md`.
- Create project folders based on the project purpose: `materials`, `assets`, and `outputs`.
- Prefer simple, reversible, project-local changes.
- Leave the project in a state that is easy to verify.

## When To Use

Use this skill for requests such as:

- "Initialize this project for Codex."
- "Set up AGENTS.md for this repo."
- "Create a standard project initialization."
- "Prepare this workspace for AI agents."
- "Make a global/default project setup skill."

Do not use this skill for full application scaffolding unless the user explicitly asks for a specific app, framework, or implementation.

## Required First Step

Before editing, state your understanding of:

1. What is being initialized.
2. What success means for this request.
3. What you will inspect before changing files.

If the request is ambiguous in a way that affects file layout, tooling, framework choice, or product behavior, ask a concise clarification question before editing.

## Inspection Checklist

Inspect only what is relevant to initialization:

- Existing `AGENTS.md`, `.codex/`, `.agents/`, `README*`, and project documentation.
- Existing `TODO.md`, `PROGRESS.md`, `materials`, `assets`, and `outputs`.
- Existing package or build files, such as `package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, or similar.
- Existing tests or CI configuration.
- Existing git status, if available.
- Existing naming, language, and documentation conventions.

Prefer fast deterministic tools for inspection. Do not infer project structure from memory when files can answer it.

## Initialization Workflow

1. Define scope
   - Identify whether the task is global skill creation, project-local setup, documentation setup, tooling setup, or a combination.
   - Avoid adding dependencies, frameworks, CI, formatters, or generators unless the user requested them or the repo already uses them.

2. Preserve existing work
   - Check whether target files already exist.
   - Read existing contents before editing.
   - Merge new guidance with existing guidance when possible.
   - Do not overwrite user changes without explicit approval.

3. Apply the smallest useful change
   - For an empty or minimally configured repo, create the required baseline files first.
   - For a repo with existing instructions, update only the directly relevant sections.
   - For global Codex setup, create a self-contained skill directory with a `SKILL.md`.
   - Create only the baseline folders that fit the project purpose, using these meanings:
     - `materials`: source materials, references, input documents, research notes, briefs, raw files, and other project inputs.
     - `assets`: reusable project assets such as images, media, icons, templates, data files, or design resources.
     - `outputs`: generated deliverables, exports, reports, builds, processed files, and final artifacts.

4. Verify
   - Confirm created or edited files exist and contain the intended content.
   - Run formatting or tests only when relevant and already available.
   - If no executable verification applies, verify by reading the files back.

5. Report
   - Summarize what changed.
   - State how it was verified.
   - State any assumptions, skipped steps, or remaining risks.

## Required Initialization Output

When initializing a project, create or update these files unless the user explicitly says otherwise:

- `README.md`: project purpose, current scope, how to use the project, and important notes.
- `AGENTS.md`: AI-agent working rules for this project.
- `TODO.md`: pending tasks, decisions, and follow-up work.
- `PROGRESS.md`: dated progress log of what has been done and verified.

Create these folders according to the project purpose:

- `materials`: project inputs and references.
- `assets`: reusable project assets.
- `outputs`: generated or final deliverables.

If a folder is not relevant to the project, state why it was skipped. If the purpose is unclear, ask before deciding which folders to create.

## Recommended File Baselines

Use these baselines as starting points. Adapt them to the actual project and preserve existing useful content.

### `README.md`

```md
# Project Name

## Purpose

Describe what this project is for.

## Structure

- `materials/`: source materials and references.
- `assets/`: reusable project assets.
- `outputs/`: generated or final deliverables.

## Notes

Add important setup, usage, or project-specific notes here.
```

### `AGENTS.md`

When creating a new project-level `AGENTS.md`, adapt this baseline to the project instead of copying blindly:

```md
# AGENTS.md

This file defines the working rules for AI agents in this project. Unless the user explicitly overrides them, all tasks should follow these rules.

## Working Rules

1. Clarify the task goal, constraints, and success criteria before making changes.
2. Prefer the simplest change that solves the current problem.
3. Modify only files and sections directly related to the task.
4. Define how completion will be verified before finishing.
5. Use code, tests, and deterministic tools for deterministic work.
6. Split large tasks into smaller checkpoints.
7. Disclose conflicting patterns or unclear conventions instead of mixing them.
8. Read relevant context before editing files.
9. Write tests or checks that verify the intended behavior when applicable.
10. Report checkpoints during multi-step work.
11. Follow existing project conventions.
12. Clearly state failures, partial verification, assumptions, and remaining risks.

## Completion Report

When finishing a task, briefly report:

1. What changed.
2. How it was verified.
3. Any remaining risks or unfinished items.
```

### `TODO.md`

```md
# TODO

## Pending

- [ ] Confirm project purpose and success criteria.

## Decisions Needed

- [ ] Record decisions that need user confirmation.
```

### `PROGRESS.md`

```md
# Progress

## YYYY-MM-DD

- Initialized project baseline.
- Verification: confirm files and folders exist.
```

## Global Skill Placement

For a personal/global Codex skill, the intended structure is:

```text
%USERPROFILE%/.codex/skills/global-project-initializer/SKILL.md
```

If filesystem permissions or sandboxing prevent writing to the global Codex skills directory, create the skill in the current workspace and report that it still needs to be installed or moved to the global skills directory.

## Guardrails

- Do not make product, architecture, or framework decisions without user confirmation.
- Do not add package dependencies for initialization alone.
- Do not reformat unrelated files.
- Do not replace existing project rules with a generic template.
- Do not overwrite existing `README.md`, `AGENTS.md`, `TODO.md`, or `PROGRESS.md`; merge or append only the necessary initialization content.
- Do not create irrelevant `materials`, `assets`, or `outputs` folders without considering the project purpose.
- Do not claim tests passed unless they were actually run and passed.
- If verification is limited to file inspection, say so explicitly.
