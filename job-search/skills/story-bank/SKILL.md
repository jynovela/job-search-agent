---
name: story-bank
description: Collect, evaluate, and improve the candidate's interview stories so every story type has a strong story ready. Use when the candidate wants to build their story bank, add or review a story, check coverage, or get feedback on how a story is pitched.
---

<goal>
Give the candidate a bank of 6–10 true, well-pitched stories in which every bucket in `story-types.md` has a primary and a backup story. Each story should be scored high enough that a hiring manager at their target level would fight for them.
</goal>

<inputs>
Read from the repo your job-search repo (set in `config.md`):
- `job-search/interview/story-types.md`: the eight buckets and the coverage goal
- `job-search/interview/story-rubric.md`: the two scales and how to give feedback
- `job-search/interview/story-bank.md`: the current bank
- `job-search/master-resume.md` and `job-search/facts.md`: the facts every story must match
- `job-search/personal-stories.md`: only when working on the outside-work answer
Do no web research.
</inputs>

<process>
Pick the mode from the candidate's ask. With no clear ask, run **Coverage** first.

**Coverage** (where the bank stands)
1. Show the coverage table from `story-bank.md`, with every empty or weak slot (a story scoring below 4 on either scale) marked.
2. Name the single most important gap. Senior loops probe 6 (Conflict & pushback), 7 (Strategy & trade-offs), and 8 (People & org building) hardest, so fill those first.
3. Offer to fill it, then move to **Collect**.

**Collect** (add a story, one at a time)
1. **Propose candidates.** For the target bucket, suggest 2–3 candidate stories from `master-resume.md`, each with its bullet ID and a one-line reason it fits. The candidate picks one or names their own.
2. **Interview for the detail bank.** Ask one question at a time and wait for each answer. Cover what made it hard, what they decided and why, the alternative they rejected, who pushed back and how they won them over, the result with numbers, and what they'd do differently. Stop once the template in `story-bank.md` is filled.
3. **Split stories that are too broad.** If a story takes over 2 minutes or spans a whole launch, split it into smaller stories that each show one point [RocketBlocks].
4. **Tag every bucket it can answer** and write the angle for each one.
5. **Evaluate it** (below), then save.

**Evaluate** (score and improve one story or the whole bank)
1. **Set the level** from the req if one is given; otherwise use the target level in `config.md`.
2. **Run the quick diagnostic** in `story-rubric.md`, then score each criterion 1–5 on both scales, citing what in the story earned the score.
3. **Give feedback** in the rubric's order: the weakest criterion first, then 2–3 concrete fixes written as replacement lines or questions to answer. If it's the wrong story for the bucket or level, say so and suggest a better candidate.
4. **Offer one rewrite** of the key beats (not a script): the 20-second setup, the decision moment, and the result line, so the candidate can hear the difference.
5. **Save.** Update the story's scores and the coverage table.

**Save** (every mode)
- Write changes to `story-bank.md`, commit with "Story bank: <what changed>" to a branch, and open a PR for the candidate to approve. Never push to the default branch or merge the PR yourself.
- When the candidate gives a new fact, number, or correction, also add it to `facts.md` or `master-resume.md` per the project rules, and tell them in one line where it went.
- End by naming the next gap to fill.
</process>

<rules>
- **Never invent.** Every number and detail comes from the files or from the candidate. Leave [number] when it's missing and ask.
- **Hold the bar.** A 3 is forgettable, so say so plainly. Praise only what earns it.
- **No scripts.** Store the facts and key beats, never a speech to memorize, because scripts break under follow-up questions [r/ExperiencedDevs].
</rules>
