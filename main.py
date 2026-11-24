"""Ship It Friday entry.

DECISION RECORD (two writing passes)

Pass 1 — four candidate commit messages, weighed against the judge's
criteria in order: (1) a git commit message from an AI coding agent, funny,
set just before breaking production on a Friday; (2) a real punch that pays
off in one read; (3) AI-agent voice: confident, cheerful, completely unaware
of the disaster about to happen; (4) Friday feeling — end-of-week rush, the
doomed urge to ship it now; (5) reads cleanly as a single line a real
engineer would recognise as a commit message.

Candidate A (90 chars):
  "feat: deploy to prod at 4:59pm Friday — tests passed on my machine, rollback plan is vibes"
  Strong: the most standard commit shape ("feat:" prefix, em-dash break);
  the classic "tests passed on my machine" joke; an exact Friday time
  (4:59pm) nails the end-of-week rush; the punch — "rollback plan is
  vibes" — is a flat, cheerful admission that there is no plan at all,
  exactly the oblivious AI-agent voice.

Candidate B (86 chars):
  "ship: Friday 4:59pm deploy, all tests green on my machine, rollback plan is just vibes"
  Strong: same joke, "just vibes" is a touch funnier. Weakness: "ship:"
  is a less standard commit prefix than "feat:", and "just" softens the
  punch — "rollback plan is vibes" stated flat lands harder than "is just
  vibes".

Candidate C (87 chars):
  "feat: ship the Friday deploy at 4:59pm, tests pass locally, prod will figure itself out"
  Strong: "prod will figure itself out" is a great oblivious-AI punch.
  Weakness: "tests pass locally" is weaker than the classic "tests passed
  on my machine", and "ship the Friday deploy" is wordier than A's
  "deploy to prod".

Candidate D (71 chars):
  "fix: remove the last safety check so Friday's deploy fits in one commit"
  Strong: dark and funny. Weakness: it reads like a human developer's
  cynical joke, not a cheerful AI agent unaware of the disaster (criterion
  3), and it never names the moment of breaking production.

Winner: Candidate A.

Pass 2 — revision of the winner: tighten "deploy to prod at 4:59pm
Friday" to "deploy to prod Friday 4:59pm" (90 -> 87 chars). The day-then-
time order is terser and more commit-message-like, and nothing is lost:
the exact Friday time, the "on my machine" joke, the em-dash break and
the "rollback plan is vibes" punch all survive. No further word can be
cut without losing either the Friday time, the test joke or the punch.

FINAL ENTRY (87 characters):
"feat: deploy to prod Friday 4:59pm — tests passed on my machine, rollback plan is vibes"

Hand count (87): "feat:" 5, " deploy" 7 (=12), " to" 3 (=15), " prod" 5
(=20), " Friday" 7 (=27), " 4:59pm" 7 (=34), " —" 2 (=36), " tests" 6
(=42), " passed" 7 (=49), " on" 3 (=52), " my" 3 (=55), " machine," 9
(=64), " rollback" 9 (=73), " plan" 5 (=78), " is" 3 (=81), " vibes" 6
(=87).
"""

import os

ENTRY = (
    "feat: deploy to prod Friday 4:59pm \u2014 tests passed on my machine, "
    "rollback plan is vibes"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
