# Lab 4 - Catch the Falling Objects

This folder contains the completed Lab 4 submission.

## Run the game

```powershell
cd catch-falling
python -m pip install -r requirements.txt
python main.py
```

Controls:

- Hold Left or Right Arrow to move the basket.
- Press Space to activate the temporary speed boost.
- Press R after game over to restart.

## Completed tasks

1. Collision detection now requires both horizontal and vertical overlap. The update loop no longer removes objects while iterating, so adjacent catches are not skipped.
2. Held-key movement is smooth and the basket remains completely inside both screen edges.
3. Objects use safe separated spawn lanes, varied spawn delays, and a seven-object on-screen limit.
4. Space activates a visible two-times speed boost for three seconds. The basket changes color, a countdown is shown, and normal speed returns automatically.

## Verification

Run the automated checks from `catch-falling`:

```powershell
python -m unittest discover -s tests -v
```

All 11 tests pass. They cover collision timing, simultaneous catches, basket boundaries, held movement, spawning rules, and the speed-boost lifecycle.

## Deliverables

- `videos/before_changes.mp4` - 10-second demonstration of the original premature collision bug.
- `videos/after_changes.mp4` - 10-second demonstration of the corrected game and added features.
- `catch-falling/` - updated source code and automated tests.
- `chat-history/Lab_4_Chat_History.pdf` - exported prompt and implementation record.

## Separate task commits

- `be4fbfe` - Task 1: fix collision detection and catch handling
- `40c1204` - Task 2: keep basket movement within screen bounds
- `2b61739` - Task 3: add controlled varied object spawning
- `b6db551` - Task 4: add temporary visible speed boost
