import copy
import shutil
import os

from templer.zope.basic_zope import BasicZope
from templer.core.base import get_var
from templer.core.vars import EASY
from templer.core.vars import EXPERT
from templer.core.vars import BooleanVar

class Plone(BasicZope):
    _template_dir = 'templates/plone'
    summary = "A project for Plone products"
    help = """
This creates a package for a basic Plone add-on project, with a 
single namespace (like Products.PloneFormGen).  To create a package 
with a nested namespace use the plone_nested_addon template.  If 
you are trying to create a Plone *site* you want to use one of the 
installers from plone.org or the ploneX_buildout (where x is the 
major version of Plone you wish to use)

To create a Plone project with a name like 'plone.app.myproject' 
(2 dots, a 'nested namespace'), use the 'plone_app' template.
"""
    category = "Plone Development"
    required_templates = ['basic_namespace']
    required_structures = ['egg_docs', 'bootstrap',]
    use_local_commands = True
    use_cheetah = True
    vars = copy.deepcopy(BasicZope.vars)
    vars.insert(5, BooleanVar(
        'add_profile',
        title='Register Profile',
        description='Should this package register a GS Profile',
        modes=(EASY, EXPERT),
        default=False,
        help="""
If your package has need of a Generic Setup profile, set this value to 'True'.  

Having a Generic Setup profile registered makes your package 'installable'
using the ZMI portal_quickinstaller or Plone's 'Add/Remove Products' control
panel.  This allows any portions of your package that require Generic
Setup--such as portlets, content types, actions and so on--to be
properly installed.
"""
    ))
    get_var(vars, 'namespace_package').default = 'collective'
    get_var(vars, 'package').default = 'example'
    
    def post(self, command, output_dir, vars):
        if vars['add_profile'] == False:
            # if we do not want a profile, remove it.            
            path = os.path.join(output_dir,
                                vars['namespace_package'],
                                vars['package'])
            try:
                shutil.rmtree(os.path.join(path, 'profiles'))
            except OSError, e:
                msg = """WARNING: Error in template rendering:

%s

Your package may have structural problems, please check before 
using it.
"""
                self.post_run_msg = msg % str(e)
            
        super(Plone, self).post(command, output_dir, vars)

