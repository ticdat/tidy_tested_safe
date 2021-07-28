# Tidy, Tested, Safe

**Tidy, Tested, Safe** is a catchphrase I invented while working for [Opex Analytics](https://www.linkedin.com/company/opex-analytics/). Part of my job requirement was to teach Industrial Engineering/Operations Research graduates to write "industrial code". The phrase "industrial code" was never explained to me, and thus I decided to study the coding practices as I found them and use my own judgement for how to best advocate for improvements. I eventually landed on the following three sentence summary.

_Write normal Python. Automate the tests. Protect against dirty data._

To give a bit more detail, I expanded these points into the  "Tidy, Tested, Safe" outline.

* **Tidy** corrects a variety of shortcomings involving code organization and style.
  * Code not organized into modules. Code that requires more than one file not organized into a Python package. Common utility routines simply copied around from project to project, as opposed to being managed as a utility library.
  * No common template for how to organize files in Github. No common strategy for how to use branches. No use of Github labels and package `__version__` to reliably identify the version of the code released to users.
  * Python scripts that weren't based around functions. Failing to take advantage of situations where a normal Python command line interface, implemented via `if __name__ == "__main__"`, was obviously appropriate. 
* **Tested** describes not only the need to test your code, but also the importance of creating automated tests. The bulk of the projects I reviewed were some form of advanced analytical engine (usually involving optimization). For such projects, the most natural form of automated testing involves creating a suite of testing data, along with a `unittest` based script that runs the engine against each of the data sets in the suite and validates the successful creation of expected results. To avoid making the perfect the enemy of the good, I emphasized meeting this basic level of regression testing. I certainly agree that the ideal analytical engine would write regression testing code well beyond the "reproducible data suite" described here.
* **Safe** addresses the problem of dirty data. It's unrealistic to assume that users will consistently abide by, or even fully understand, the pre-requirements of an advanced analytical engine. The code must reliably identify and explain data integrity problems both to the user (when deployed as an app) and to the developer (during development and debugging).

As it happens, I had encountered these problems myself when I first began writing engines in Python a few years prior. I created the open source package `ticdat` precisely to address these concerns. Thus, a lot of my advice boiled down to "Use `ticdat` the way I do.". However, the principles of Tidy, Tested, Safe are worth understanding, even if you never use Python at all. In essence, I was advocating for Computer Science best practices, as they related to IEOR. 
