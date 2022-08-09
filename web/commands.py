import click


@click.group()
def web():
    """Commands for the web application"""


@web.command()
def do():
    """Command description here"""

    click.echo('Doing')
