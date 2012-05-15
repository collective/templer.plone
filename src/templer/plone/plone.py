import copy

from templer.core.base import get_var
from templer.core.vars import EASY
from templer.core.vars import EXPERT
from templer.core.vars import BooleanVar
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
    get_var(vars, 'namespace_package').default = 'collective'
    get_var(vars, 'package').default = 'example'

    def pre(self, command, output_dir, vars):
        super(Plone, self).pre(command, output_dir, vars)
        vars['use_localcommands'] = self.use_local_commands


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
    get_var(vars, 'package').default = 'example'
