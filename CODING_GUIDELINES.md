# Coding Guidelines
This document contains all of the coding guidelines that we have followed in the construction of this project. We largely follow PEP 8 conventions.

## Naming conventions
- Variables will be named appropriately and use a lowercase word or words. Words will be seperated with underscores. E.g. variable, variable_example

- Functions will be named appropriately and use a lowercase word or words. Words will be seperated with underscores. E.g. fucntion, fucntion_example

- Methods will be named appropriately and use a lowercase word or words. Words will be seperated with underscores. E.g. method, method_example

- Classes will be named appropriately and start with a capital letter. Words will not be seperated. E.g. Class, ClassExample

- Constants will be named appropriately and will be uppercase. Words will be seperated with underscores. E.g. CONSTANT, CONSTANT_EXAMPLE

## Code layout
- Top level functions and classes should be surrounded by two blank lines
- Methods inside classes should be surrounded by a single blank line
- Lines shouldn't be more than 120 characters long
- Indentations should be equal to 4 spaces

## Comments
- Use block comments to document a small section of code
- Docstrings should be used for all public modules, functions, classes and methods. Docstrings should contain the author, what it returns, and a high-level summary

## Whitespace
- Whitespace should not be used around comparisons E.g. x<3, not x < 3
- Commas should be followed by, but not proceeded by a space. E.g. 1, 2, 3 not 1,2,3 or 1 , 2 , 3
- All jinja code in html should have a single whitespace surrounding the contents of the code. E.g. { current_user.dob }}, not {{current_user.dob}}

## Linters
We used Pylint as our linter to ensure that we follow Pep8 guidelines so that our code is readable and consistent

## HTML and CSS Guidelines
- Use lowercase for all HTML tags and attributes.
- Class names in HTML and CSS should be descriptive and use lowercase letters, with words separated by hyphens (-). E.g., .header-section, .main-content.
- IDs in HTML and CSS should be used sparingly and be unique within the document. ID names should be descriptive and use lowercase letters, with words separated by hyphens (-). E.g., #navigation-menu, #footer-section.
- Use semantic HTML elements whenever possible (e.g., <header>, <nav>, <main>, <footer>).
- CSS properties should be organized logically and consistently.
- Use shorthand properties where possible to keep the code concise (e.g., use 'margin' instead of 'margin-top', 'margin-bottom', 'margin-left', 'margin-right').
- CSS should be written in an external stylesheet rather than inline whenever possible.
- Avoid using inline styles except where absolutely necessary.