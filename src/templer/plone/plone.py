import copy

from templer.core.base import get_var
from templer.core.vars import EASY
from templer.core.vars import EXPERT
from templer.core.vars import BooleanVar
from templer.core.vars import StringVar
from templer.zope import BasicZope
from templer.zope import NestedZope


try:
    from templer.localcommands import SUPPORTS_LOCAL_COMMANDS
    from templer.localcommands import LOCAL_COMMANDS_MESSAGE
except ImportError:
    SUPPORTS_LOCAL_COMMANDS = False


PLONE_HELP_TEXT = """
This template creates a package for a basic Plone add-on project with
a single namespace (like Products.PloneFormGen).

To create a Plone project with a name like 'collective.geo.bundle'
(2 dots, a 'nested namespace'), use the 'plone_nested' template.
"""


NESTED_HELP_TEXT = """
This template creates a package for a basic Plone add-on project with a
nested namespace (two dots, like 'collective.geo.bundle')

To create a Plone project with a name like 'Products.PloneFormGen use
the 'plone_basic' template.
"""


POST_RUN_TEXT = """"""


GS_PROFILE_HELP = """
If your package has need of a Generic Setup profile, set this value
to 'True'.

Having a Generic Setup profile registered allows your package to be
'activated' using Plone's 'Add/Remove Products' control panel.
This allows any portions of your package that require Generic
Setup--such as portlets, content types, actions and so on--to be
properly installed.
"""


if SUPPORTS_LOCAL_COMMANDS:
    PLONE_HELP_TEXT += """
This template supports local commands.  These commands allow you to
add Plone features to your new package.
"""
    POST_RUN_TEXT = LOCAL_COMMANDS_MESSAGE


PLONE_BUILDOUT_WARNING = """
If you are trying to create a Plone *site* then the best place to
start is with one of the Plone installers.  If you want to build
your own Plone buildout, use one of the plone'N'_buildout templates
"""


ROBOT_HELP = """
If you would like to have functional testing enabled in your package,
based on the Robot framework, set this value to 'True'.

By default tests will be started with Firefox, and will check that
the text 'Plone site' is present on the Plone home page.

The following tutorial covers writing your own tests:
http://ploneact.readthedocs.org/en/latest/tutorial.html
"""


class Plone(BasicZope):
    _template_dir = 'templates/plone'
    summary = "A package for Plone add-ons"
    help = PLONE_HELP_TEXT + PLONE_BUILDOUT_WARNING
    post_run_msg = POST_RUN_TEXT
    category = "Plone Development"
    required_templates = ['basic_namespace']
    default_required_structures = ['egg_docs', 'bootstrap', ]
    use_local_commands = SUPPORTS_LOCAL_COMMANDS
    use_cheetah = True
    vars = copy.deepcopy(BasicZope.vars)
    vars.insert(5, BooleanVar(
        'add_profile',
        title='Register Profile',
        description='Should this package register a GS Profile',
        modes=(EASY, EXPERT),
        default=False,
        structures={'False': None, 'True': 'namespace_profile'},
        help=GS_PROFILE_HELP,
    ))
    vars.insert(6, BooleanVar(
        'add_robot_tests',
        title='Robot Tests',
        description='Should the default robot test be included',
        modes=(EASY, EXPERT),
        default=False,
        help=ROBOT_HELP,
    ))
    get_var(vars, 'namespace_package').default = 'collective'
    get_var(vars, 'package').default = 'example'

    def pre(self, command, output_dir, vars):
        super(Plone, self).pre(command, output_dir, vars)
        vars['use_localcommands'] = self.use_local_commands
        vars['classname'] = (vars['namespace_package'] + vars['package'])\
            .title().replace(" ", "")


class NestedPlone(NestedZope):
    _template_dir = 'templates/nested_plone'
    summary = "A package for Plone add-ons with a nested namespace"
    help = NESTED_HELP_TEXT + PLONE_BUILDOUT_WARNING
    category = "Plone Development"
    required_templates = ['nested_namespace']
    default_required_structures = ['egg_docs', 'bootstrap', ]
    use_local_commands = False
    use_cheetah = True
    vars = copy.deepcopy(NestedZope.vars)
    vars.insert(5, BooleanVar(
        'add_profile',
        title='Register Profile',
        description='Should this package register a GS Profile',
        modes=(EASY, EXPERT),
        default=False,
        structures={'False': None, 'True': 'nested_namespace_profile'},
        help=GS_PROFILE_HELP,
    ))
    get_var(vars, 'namespace_package').default = 'collective'
    get_var(vars, 'namespace_package2').default = 'nested'
    get_var(vars, 'package').default = 'example'


class PloneTile(Plone):
    _template_dir = 'templates/plone_tile'
    vars = copy.deepcopy(Plone.vars)
    get_var(vars, 'add_profile').default = True
    get_var(vars, 'add_profile').modes = []
    vars.insert(5, StringVar(
        'tile_title',
        title='Tile title',
        description='The human readable title of the tile.',
        modes=(EASY, EXPERT),
        default="My tile",
    ))

    def pre(self, command, output_dir, vars):
        super(PloneTile, self).pre(command, output_dir, vars)
        vars['tile_classname'] = vars['tile_title'].title().replace(" ", "")
        vars['namespace_package_uppercase'] = \
            vars['namespace_package'].upper()
        vars['package_uppercase'] = vars['package'].upper()
