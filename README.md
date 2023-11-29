# GDFetch
A terminal fetch to display information about Geometry Dash extreme demons
## Dependecies
- [pointercratepy](https://github.com/bretheskevin/pointercrate.py)
- [typer](https://github.com/tiangolo/typer)
- [rich](https://github.com/Textualize/rich)
## About
Simple script to pull up and print information about a level on the Pointercrate demon list. I made this to get more comfortable with programming outside of the context of game development. I've only tested on Arch Linux, so let me know if you run into problems on other operating systems.
## Usage
To search by name: (NOTE: Case sensitive, and if the name is multiple words long you should use quotations)
```
python GDFetch.py name <name>
```
To search by placement on the demon list:
```
python GDFetch.py position <position>
```
