.. |pypi_download| image:: https://img.shields.io/pypi/dm/trame-datagrid

==========================================
trame-datagrid |pypi_download|
==========================================

Trame widget of the `RevoGrid <https://revolist.github.io/revogrid/>`_ component for vue3.

.. image:: https://raw.githubusercontent.com/Kitware/trame-datagrid/master/docs/trame-datagrid.png
  :alt: Example with fake data of what it looks like

License
-----------------------------------------------------------

trame-datagrid is made available under the MIT License. For more details, see LICENSE This license has been chosen to match the one use by RevoGrid which is instrumental for making that library possible.

Installing
-----------------------------------------------------------

trame-datagrid can be installed using pip

.. code-block:: console

    pip install trame-datagrid


Development
-----------------------------------------------------------

This component require to build a JavaScript library that bundles RevoGrid into a standalone file that can then be used by trame directly.

Build and install the Vue components

.. code-block:: console

    cd vue-components
    npm i
    npm run build
    cd -

Install the application

.. code-block:: console

    pip install .


Community
-----------------------------------------------------------

`Trame <https://kitware.github.io/trame/>`_ | `Discussions <https://github.com/Kitware/trame/discussions>`_ | `Issues <https://github.com/Kitware/trame/issues>`_ | `Contact Us <https://www.kitware.com/contact-us/>`_

.. image:: https://zenodo.org/badge/410108340.svg
    :target: https://zenodo.org/badge/latestdoi/410108340


Enjoying trame?
-----------------------------------------------------------

Share your experience `with a testimonial <https://github.com/Kitware/trame/issues/18>`_ or `with a brand approval <https://github.com/Kitware/trame/issues/19>`_.


JavaScript dependency
-----------------------------------------------------------

This Python package bundle the ``@revolist/vue3-datagrid@3.0.97`` JavaScript library. If you would like us to upgrade it, `please reach out <https://www.kitware.com/trame/>`_.
