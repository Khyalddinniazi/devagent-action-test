# devagent live demo 🤖

This repository is a **live demo of [devagent](https://github.com/Khyalddinniazi/devagent)**, a tool
that turns a GitHub issue into a tested pull request using a team of sandboxed AI agents.

Nobody wrote the code for the feature below by hand. Someone added a label, and devagent did the rest.

## What happened

| Step | Link |
|---|---|
| 1. An issue asked for a new function, and someone added the `devagent` label | [Issue #1: Add an is_palindrome(text) function](https://github.com/Khyalddinniazi/devagent-action-test/issues/1) |
| 2. GitHub Actions started devagent on a macOS runner: plan → code → tests → secret scan | [The workflow run](https://github.com/Khyalddinniazi/devagent-action-test/actions/runs/42425367002) (1 min 25 s) |
| 3. devagent opened a PR with the function, 6 new tests and a note for reviewers, then commented the link on the issue ($0.41) | [Pull request #2](https://github.com/Khyalddinniazi/devagent-action-test/pull/2) |
| 4. A human reviewed and merged it, and the issue closed automatically (`Closes #1`) | devagent never merges by itself |

## How it's set up

- The whole setup is one workflow file: [.github/workflows/devagent.yml](.github/workflows/devagent.yml).
- Only people with write access can start it.
- The issue text is treated as untrusted. It can't inject shell commands or switch devagent's options.
- The agents run in a sandbox with no network access, and there's a spending limit for each run.
- More details: [devagent's GitHub Action guide](https://github.com/Khyalddinniazi/devagent/blob/main/docs/GITHUB_ACTION.md).

## The project itself

`textkit` is a tiny practice library of text helpers (`word_count`, `is_palindrome`). Run its tests
with `pytest`.
