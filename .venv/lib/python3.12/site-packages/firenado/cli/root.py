from cartola.config import load_yaml_file
import click
import firenado.conf
import logging
import os
import taskio
import sys

pass_context = click.make_pass_decorator(taskio.CliContext, ensure=True)


@taskio.root(root="firenado", taskio_conf=firenado.conf.taskio)
def firenado_cli(ctx):
    pass
