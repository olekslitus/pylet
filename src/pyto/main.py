import click


@click.group()
@click.version_option()
def cli():
    """pyto - python command tools"""
    pass


@cli.command(no_args_is_help=True)
def init():
    """Initialize a new project in this directory"""
    click.echo('Init')


@cli.command(no_args_is_help=True)
def adopt():
    """Adopt the current setup of the package"""
    click.echo('Adopt')


@cli.command()
@click.option('--pkg-name', prompt='Package name')
@click.option('--git-ignore', prompt='Add .gitignore?')
def new(pkg_name, git_ignore):
    """Create a new project in specified directory"""
    click.echo(pkg_name)


@cli.command(no_args_is_help=True)
def build():
    """Build the project"""
    click.echo('Build')


@cli.command(no_args_is_help=True)
def graph():
    """Show dependecy graph of the project"""
    click.echo('Graph')


@cli.command(no_args_is_help=True)
def install():
    """Install all packages"""
    click.echo('Install')


@cli.command(no_args_is_help=True)
def uninstall():
    """Uninstall all packages"""
    click.echo('Uninstall')


@cli.command(no_args_is_help=True)
def env():
    """Create virtual evirment"""
    click.echo('Envs')


@cli.command(no_args_is_help=True)
@click.option('--no-checks', is_flag=True, show_default=True, default=False, help="Run without checks.")
@click.argument('target')
def run(no_checks, target):
    """Run scripts"""
    click.echo('Run')


@cli.command(no_args_is_help=True)
def clean():
    """Clean env from unused dependecies"""
    click.echo('Clean')


@cli.command(no_args_is_help=True)
@click.argument('target')
def check(target):
    """Perform static check of the target"""
    click.echo('Check')


@cli.command(no_args_is_help=True)
def docs():
    """Generate docs"""
    click.echo('Docs')


@cli.command(no_args_is_help=True)
@click.argument('package')
def add(package):
    """Add new dependency"""
    click.echo('Add')


@cli.command(no_args_is_help=True)
def pin():
    """Pin requirements"""
    click.echo('Pin')


@cli.command(no_args_is_help=True)
@click.option('--dry-run', is_flag=True, show_default=True, default=False, help="Dry run, do not publish")
@click.option('--test-pypi', is_flag=True, show_default=True, default=False, help="Publish to test PyPi")
def publish():
    """publish package"""
    click.echo('Publish')