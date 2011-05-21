import os
import copy

from templer.plone import Plone
from templer.core.base import get_var
from templer.core.vars import var, StringVar, EASY, EXPERT

class Archetype(Plone):
    _template_dir = 'templates/archetype'
    summary = 'A Plone project that uses Archetypes content types'
    help = """
This creates a Plone project that uses Archetypes content types.
It has local commands that will allow you to add content types
and to add fields to your new content types.
"""
    post_run_msg = """
There is a local command to add individual Archetype content types
and to add fields to those content types. See the instructions above
on how to use this command.
"""

    required_templates = ['plone_basic']
    use_cheetah = True
    # use_local_commands = True

    vars = copy.deepcopy(Plone.vars)
    vars.insert(1, StringVar(
        'title',
        title='Project Title',
        description='Title of the project',
        modes=(EASY, EXPERT),
        default='Example Name',
        help="""
This becomes the title of the project. It is used in the 
GenericSetup registration for the project and, as such, appears
in Plone's Add/Remove products form.
"""
       )
       )
    #zope2product should always defaults to True
    get_var(vars, 'zope2product').default = True
    #add_profile should always default to True for archetype packages
    get_var(vars, 'add_profile').default = True
    #add_profile need not appear as a question for archetype packages
    get_var(vars, 'add_profile').modes = (EXPERT,)
