#!/usr/bin/env python
from flask import redirect, url_for


print redirect(url_for('login'))