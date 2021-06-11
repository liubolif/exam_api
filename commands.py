import click
from flask.cli import with_appcontext

from app import db

@click.group()
def cli():
    pass


@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()
    click.echo("tables created!!!")


cli.add_command(create_tables)

if __name__ == '__main__':
    cli()
