Installing
----------

1) First, install
   **`autopep8 <http://pypi.python.org/pypi/autopep8/>`_**

from pip:

::

    pip install --upgrade autopep8

from easy\_install:

::

    easy_install -ZU autopep8

Notice: Sublime is using python 2.6 defaultly. Use easy\_install-2.6 or
pip-2.6

::

    easy_install-2.6 pip

    pip-2.6 install --upgrade autopep8

    easy_install-2.6 -ZU autopep8

2) Then install this Sublime plugin

**With the `Package Control
plugin <http://wbond.net/sublime_packages/package_control>`_:** Add `my
package
channel <https://github.com/cancerhermit/Sublime-package-channel>`_ url
-

::

    https://raw.github.com/cancerhermit/Sublime-package-channel/master/repositories.json

Bring up the Command Palette (``Command+Shift+P`` on OS X,
``Control+Shift+P`` on Linux/Windows). Select "Package Control: Install
Package", wait while Package Control fetches the latest package list,
then select **Autogit** when the list appears. The advantage of using
this method is that Package Control will automatically keep plugins up
to date with the latest version.

**Without Git:** Download the latest source from
`GitHub <https://github.com/cancerhermit/Sublime-autopep8>`_ and copy
the Sublime-autopep8 folder to your Sublime Text "Packages" directory.

**With Git:** Clone the repository in your Sublime Text "Packages"
directory:

::

    git clone https://github.com/cancerhermit/Sublime-autopep8.git

The "Packages" directory is located at:

-  OS X:

   ::

       ~/Library/Application Support/Sublime Text 2/Packages/

-  Linux:

   ::

       ~/.config/sublime-text-2/Packages/

-  Windows:

   ::

       %APPDATA%/Sublime Text 2/Packages/

Usage
-----

Just save. Plugin use **on\_post\_save** EventListener
