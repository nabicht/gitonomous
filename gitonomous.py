
# Metonomous
# meta data of a project
#  +
# acting independently or having the freedom to do so

"""
A module is a self contained set of meta-functionality of a software development
 project. Each module is:
  1) a sub-directory in the code-base (under meta-one)
  2) how to parse the data into the object model for tools to use (can I just
     do this by enforcing yaml or something?)
  3) example object
  4) determine if the object is even readable

A Module object needs:
  1) Directory name
  2) Example

It is important that everything can be used by a human without any other tools
 and that everything can be done manually. Any tool is just a power tool: it
 makes it quicker/speeds up work but can still be done manually.

For simplicity sake, each record/data entry of a module is its own file


Portability and use as anyone wants is key. So the data needs to be simple
 flat files, easily human readable, easily human editable, and still easy for
 applications, ad-hoc scripts, etc. to use.

Flexability is important:
  - don't have validation of Modules limit adding new tags. If someone wants to
     add a "status" tag to a DevLog then let them.
  - Want the ability to have mulitple entries per file, so use yaml load all
  - files that arent' part of metonomous in the directories without breaking
     stuff
"""

# TODO I don't know what my object model looks like or if I even need one so I'm
 just going to start coding and see what functionality demands

import errno
import os
import os.path
import datetime.datetime

class DevLog:

    REQUIRED_FIELDS = {'timestamp', 'body'}
    OPTIONAL_FIELDS = {'title','author', 'tags'}

    def dir(): return "dev_log"

    # TODO for flexiblity it probably makes sense for examples to be actual files that get written into the directory
    def examples():
        no_title = {'timestamp': datetime.datetime.now(),
                    'body': "If you want to track your development and your thoughts on what youare coding you can do it right here.\n\nThis is the body of a development log entry."
                    }
        with_title = {'timestamp': datetime.datetime.now(),
                      'title': 'Some development logs have titles',
                      'body': "if you want to sum up your log with a nice title, then you can do it just like this."
                      }
        all_options = {'timestamp': datetime.datetime.now(),
                       'title': 'All the options',
                       'body': "There are ."
                       }

    # TODO do I want to validate data fields? like timestmap to make sure type is right?
    def validate(data): return REQUIRED_FIELDS <= set(data)

class Tasks:

    REQUIRED_FIELDS = {'name', 'description', 'type'}
    OPTIONAL_FIELDS = {'due_date', 'comments', 'status', 'tags', 'reporter', 'assigned'}

    def dir(): return "tasks"

    def validate(data): return REQUIRED_FIELDS <= set(data)

class Docs:
    def dir(): return "docs"

MODULES = {DevLog, Tasks, Docs}

def create(directory, project_name, modules):
    # check if directory exists
    if not os.path.isdir(directory):
        raise Exception("The specified directory to contain the project (%s) does not exist." % directory)

    # make directory for project name
    project_dir = os.path.join(directory, project_name)
    try:
        os.mkdir(project_dir)
    except OSError as e:
        if e.errno == errno.EEXIST:
            raise Excpetion("Project directory (%s) already exists." % project_dir)
        else:
            raise e

    # make the structure of the project sub directories
    os.mkdir(os.path.join(project_dir, "src"))
    meto_dir = os.path.join(project_dir, "metonomous")
    os.mkdir(meto_dir)

    # TODO this seams like somethign that could be automated with module objects
    # make the module directories
    for module in MODULES:
        os.mkdir(os.path.join(meto_dir, module.dir()))


    # TODO make the example data in the module
