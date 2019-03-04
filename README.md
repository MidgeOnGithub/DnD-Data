## DnD Data
A simple set of Python scripts and resulting JSON string files with data related to DnD.
More specifically, data regarding official 5th Edition Wizards of the Coast publications (excluding experimental "Unearthed Arcana").
Intended for use in a programs which load in said JSON strings, then extract or pretty-print entries within them.

### Disclaimer
The contents of this repo are not intended to represent an official *Dungeons and Dragons* nor *Wizards of the Coast* product.
All product and company names are trademarks™ or registered trademarks® of their respective holders.
Use of them does not imply any affiliation with nor endorsement by them.

### Race
Each entry in the `races` file is structured such that the "base" object [a playable race] contains values that may be overwritten or modified by "sub" dictionaries `subraces` within them.
> If provided, subraces *must* be chosen: `Sea Elf` is a proper race choice, `Elf` is not.

Every complete race should contain the following entries
(assuming, per above, a subrace adds or overwrites values from the "base" race):
> * Race Name
>   * Subrace string should be placed before "base" race to create the full name when printing
> * Ability Modifiers
> * Lifespan
>   * Presented as a string in case literature gives a range instead of a value, must be parsed
> * Size
>   * Tier
>     * (Small, etc.)
>   * Height and Weight
>     * Base and Roll Modifiers
> * Speed
>   * Standard
>   * Climbing, Flying, Swimming
>     * null unless they overwrite the default given by movement penalties per the PHB

### Future Development
This repo will eventually contain data regarding DnD `classes`. Addition of other data is unlikely but possible.
