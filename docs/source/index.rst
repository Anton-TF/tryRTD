Welcome to Lumache's documentation!
===================================

Versioning
----------

This is version #2

Intersphinx
-----------

Few intersphinx links 

 - sphinx : referece = :ref:`sphinx:ref-role`
 - : doc : sphinx:usage/extensions/intersphinx = :doc:`sphinx:usage/extensions/intersphinx`


PlantUML
--------

.. uml::

    @startuml
    Alice -> Bob: Authentication Request
    Bob --> Alice: Authentication Response

    Alice -> Bob: Another authentication Request
    Alice <-- Bob: Another authentication Response
    @enduml

**Lumache** (/lu'make/) is a Python library for cooks and food lovers
that creates recipes mixing random ingredients.
It pulls data from the `Open Food Facts database <https://world.openfoodfacts.org/>`_
and offers a *simple* and *intuitive* API.

Check out the :doc:`usage` section for further information, including
how to :ref:`installation` the project.

.. note::

   This project is under active development.

Contents
--------

.. toctree::

   usage
   api
