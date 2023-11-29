from pointercratepy import Client
import typer
from rich import print

client = Client()

app = typer.Typer()

ascii_art = []

# ASCII art goes there :3
ascii_art.append("[blue]██████████████[/blue]")
ascii_art.append("[blue]██[/blue]          [blue]██[/blue]")
ascii_art.append("[blue]██[/blue]          [blue]██[/blue]")
ascii_art.append("[blue]██[/blue] [blue]███[/blue]  [blue]███[/blue] [blue]██[/blue]")
ascii_art.append("[blue]██[/blue]          [blue]██[/blue]")
ascii_art.append("[blue]██[/blue] [blue]████████[/blue] [blue]██[/blue]")
ascii_art.append("[blue]██[/blue]          [blue]██[/blue]")
ascii_art.append("[blue]██████████████[/blue]")

def print_demon_info(level: list):

    print(ascii_art[0] + "   " + "[bold red]-----GDFETCH-----[/bold red]")

    print(ascii_art[1] + "   " + "[bold green]Name:[/bold green] " + level[0].get("name"))

    print(ascii_art[2] + "   " + "[bold green]Created By: [/bold green]" + level[0].get("publisher").get("name"))

    print(ascii_art[3] + "   " + "[bold green]Verified by: [/bold green]" + level[0].get("verifier").get("name"))

    print(ascii_art[4] + "   " + "[bold green]Position: [/bold green]" + str(level[0].get("position")))

    print(ascii_art[5] + "   " + "[bold green]Video: [/bold green]" + level[0].get("video"))

    print(ascii_art[6])

    print(ascii_art[7] + "   " + "[red]by hazelbestiee ^_^[/red]")

@app.command("position")
def fetch(pos: int):
    
    level = Client.get_demons(before=pos+1, after=pos-1)

    print_demon_info(level)

@app.command("name")
def fetch(lvl_name: str):

    level = Client.get_demons(name=lvl_name)

    print_demon_info(level)

if __name__ == "__main__":
    app()