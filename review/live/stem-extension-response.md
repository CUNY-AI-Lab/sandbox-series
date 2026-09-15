I retrieved Newton: Experimental Variants and the supporting Newton: Light and Colour source, then built the extension.

## Historical source

The aperture comparison draws on Newton: Experimental Variants, which records Moray's proposals and Newton's replies on changing the apparatus, including aperture [3]. Newton's original Letter (Light and Colour) describes admitting sunlight through a small opening, forming the spectrum, and investigating aperture size among possible causes of the effect [4].

## What changed

- Added one new action: `compare aperture`.
- It requires the `spectrum` flag and the `screen` item.
- It sets a new flag `aperture_compared`, added to `goal_flags`.
- `aperture_compared` is cleared when the shutter closes, so the comparison must be repeated after reopening.
- Other actions and rules are unchanged except for the laboratory description and completion text now mentioning the aperture step.

## Winning sequence

1. `north` → `take prism` → `take screen`
2. `south` → `east`
3. `open shutter`
4. `use prism` (sets `spectrum`)
5. `use screen` (sets `red_selected`)
6. `compare aperture` (sets `aperture_compared`)
7. `test red light` (sets `red_tested`)
8. `record result` (sets `recorded`)

## Blocked action

After `open shutter` but before `use prism`, entering `compare aperture` fails: the `spectrum` flag is not set and the `screen` item is not held.

## Historical limits

- The laboratory, rooms, inventory, commands, and winning condition are invented [4].
- The single screen and single prism simplify Newton's apparatus of two pierced boards and two prisms [4].
- The aperture comparison observes that breadth changes while length stays much the same; it is a scripted observation, not a physical measurement, and one controlled change rules out an alternative rather than proving causation [3].

No command tests have been run; this scenario is a candidate until its commands execute successfully.


The playable extension is now rendered above with the added `compare aperture` action.

Reminder: the embedded game is self-contained — enter commands inside it. To review a run, select **Discuss record**, send the record, and I'll identify an observed decision, its prerequisite, a source comparison, and one limitation.
