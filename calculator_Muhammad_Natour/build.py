from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")

name = "calculator_Muhammad_Natour"
version = "0.1"
default_task = "publish"


@init
def initialize(project):
    project.set_property("dir_source_unittest_python", "tests/unittest/calculator_Muhammad_Natour")
    project.set_property("unittest_module_glob", "test_*.py")
