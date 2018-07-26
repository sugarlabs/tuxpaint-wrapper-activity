What is this?
=============

Tux Paint wrapper starts the Tux Paint application for the Sugar desktop.

How to use?
===========

Tux Paint wrapper is not part of the Sugar desktop, but can be added.  Please refer to;

* [How to Get Sugar on sugarlabs.org](https://sugarlabs.org/),
* [How to use Sugar](https://help.sugarlabs.org/),

How to upgrade?
===============

On Sugar desktop systems;
* Install Tux Paint using your operating system package management tools,
* Clone this repository,
* Move the clone repository to the ~/Activities directory,

For example, on Ubuntu;

```
sudo apt install --yes tuxpaint git
git clone --depth=1 https://github.com/sugarlabs/tuxpaint-wrapper-activity
rm -r ~/Activities/TuxPaint.activity
mv tuxpaint-wrapper-activity ~/Activities/TuxPaint.activity

```

How to integrate?
=================

Tux Paint wrapper depends on Python, [Sugar Toolkit for GTK+ 3](https://github.com/sugarlabs/sugar-toolkit-gtk3), and Tux Paint.
