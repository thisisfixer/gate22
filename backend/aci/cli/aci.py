import click

from aci.common.logging_setup import setup_logging

setup_logging()


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
def cli() -> None:
    pass


if __name__ == "__main__":
    cli()
