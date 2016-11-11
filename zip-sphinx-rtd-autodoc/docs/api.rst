********************
gsw_py_mat Functions
********************

This section documents the Python and Matlab functions that are available in the :kbd:`gsw_py_mat`.


Python Function
===============

.. automodule:: gsw_py_mat.py_cmd
    :members:


Matlab Functions
================

.. function:: gsw_py_mat.startup()

    Matlab startup function that provides access to the Matlab GSW3 library.

    .. note:: Only works on machines that have access :file:`/ocean/`.


.. function:: gsw_py_mat.mw_gsw_CT_from_t(filename, SA, t, p)

    Calculate conservative temperature from absolute salinity,
    in situ temperature,
    and pressure.

    :arg filename: Name of file in which Matlab script will store its
                   results.

    :arg SA: Absolute salinity.

    :arg t: Temperature.

    :arg p: Pressure.


.. function:: gsw_py_mat.mw_gsw_SA_from_SP(filename, SP, p, lon, lat)

    Calculate absolute salinity from practical salinity and pressure
    with corrections based on longitude and latitude.

    :arg filename: Name of file in which Matlab script will store its
                   results.

    :arg SP: Practical salinity.

    :arg p: Pressure.

    :arg lon: Longitude of the location at which the salinity is to be
              calculated.

    :arg lat: Latitude of the location at which the salinity is to be
              calculated.
