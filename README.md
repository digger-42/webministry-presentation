# Web Ministry Training

Slides, handouts and demos for internal training of the Web Ministry Team: the people who help maintain the website.

Decks are LibreOffice Impress (`.odp`); supporting material is Writer (`.odt`) and Calc (`.ods`), plus images, screen recordings and HTML demo pages.

## Git LFS

Office files, images and video are stored with [Git LFS](https://git-lfs.com) (see `.gitattributes`). Run this once per machine before cloning:

```sh
git lfs install
```

## Layout

- `templates/PCC-WebMinistry.otp`: the Impress template, built from PCC Graphic Standards 2020
- `deck/WebMinistry-Training.odp`: the training deck
- `assets/brand/`: logos and the tree watermark used by the template
- `tools/build_template.py`: regenerates the template and starter deck (`python3 tools/build_template.py`, needs LibreOffice)

## Fonts

The brand typeface is Avant Garde. The template uses **TeX Gyre Adventor**, its free look-alike. Install it before opening the deck, or LibreOffice will substitute another font:

- Linux: `sudo apt install fonts-texgyre`
- Windows or Mac: download from [GUST](https://www.gust.org.pl/projects/e-foundry/tex-gyre/adventor) and install the `.otf` files

## Master slides

| Master | Use |
| --- | --- |
| PCC-Title | Title slide: tree watermark, logo, title and date |
| PCC-Section | Section divider: dark background, reversed logo |
| PCC-Content | Default content slide, green accent |
| PCC-Content-Gold | Part 1: people |
| PCC-Content-Teal | Part 2: the building |
| PCC-Content-Burgundy | Part 3: services |
| PCC-Content-DarkGreen | Part 4: the website |

The logo PNGs were cut from the brand guide PDF. Swap in the official files from Ken Stewart when available, keeping the same filenames, and rerun the build.
