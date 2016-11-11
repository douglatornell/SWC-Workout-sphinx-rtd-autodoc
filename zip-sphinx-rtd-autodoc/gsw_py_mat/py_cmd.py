"""Python interface to Matlab GSW functions.
"""
import shlex


def make_matlab_cmd(scriptname, filename, args):
    """Return a command to run the Matlab script :kbd:`scriptname`.

    :arg str scriptname: Name of the Matlab script to make the command for.

    :arg str filename: Name of file in which Matlab script will store its
                       results.

    :arg list args: Arguments to pass to the Matlab script.

    :returns: Command suitable to be passed to :py:func:`subprocess.run`.
    :rtype: list
    """
    singlequote = "'"
    comma = ','

    # add quotes to the filename
    mfilename = '{0}{1}{0}'.format(singlequote, filename)

    firstpart = '{0}('.format(scriptname)
    lastpart = ');exit'

    functioncall = firstpart + mfilename
    for arg in args:
        functioncall += comma + str(arg)
    functioncall += lastpart

    cmd = shlex.split('matlab -nodesktop -nodisplay -r')
    cmd.append(functioncall)
    return cmd
