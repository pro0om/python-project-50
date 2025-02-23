### Hexlet tests and linter status:
[![Actions Status](https://github.com/pro0om/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/pro0om/python-project-50/actions)

[![Check_my_Actions](https://github.com/pro0om/python-project-50/actions/workflows/check.yml/badge.svg)](https://github.com/pro0om/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/494bdd544175e66ad82b/maintainability)](https://codeclimate.com/github/pro0om/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/494bdd544175e66ad82b/test_coverage)](https://codeclimate.com/github/pro0om/python-project-50/test_coverage) 

# GENDIFF (Difference Generator)

The package contains the program that outputs the differences between two files (JSON or YAML) in several possible formats. Available formats: stylish (default), plain, json.

## Requirements:

* python = "^3.10"* 
* pip = "^25.0"

## To git clone use:

`git clone git@github.com:pro0om/python-project-50.git`

## Use commands for different formats:

1. stylish(Default):
    `gendiff tests/fixtures/file3.json tests/fixtures/file4.json`
2. json:
    `gendiff tests/fixtures/file3.json tests/fixtures/file4.json -f json`
3. plain:
    `gendiff tests/fixtures/file3.json tests/fixtures/file4.json -f plain`
