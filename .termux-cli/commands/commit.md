---
description: Create a git commit
argument-hint: [message]
allowed-tools: Bash(git:*)
---

Current git status:
!`git status --short`

Current git diff:
!`git diff --stat`

Create a well-formatted git commit with message: $ARGUMENTS

Follow conventional commits format if no message provided.
