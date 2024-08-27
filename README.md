# copier-kedro

[Copier](https://github.com/copier-org/copier) template Kedro projects.

_As simple as possible. No magic._

## Usage

```
mkdir my-kedro-project && cd my-kedro-project
uvx copier copy --trust gh:astrojuanlu/copier-kedro .
```

✨

(`uvx` is the shorthand for `uv tool run`, see [the uv documentation](https://docs.astral.sh/uv/guides/tools/))

## Features

- [uv] for project management.
- [pytest] for testing.
- [tox] for automation of test runners and other stuff.
- [Sphinx] for documentation
- [GitHub Actions] for continuous integration and publishing to PyPI.
- [Read the Docs] for continuous documentation.
- [mypy] for type checks.
- [ruff] for style checks and automatic Python code formatting.
- [pre-commit] for optional automation of style checks.
- [PDM] as build backend.

## License

[MIT License](LICENSE)

[uv]: https://github.com/astral-sh/uv
[copier]: https://github.com/copier-org/copier/
[mypy]: http://mypy.readthedocs.io/
[PDM]: https://pdm-project.org/
[pytest]: https://docs.pytest.org/
[Sphinx]: http://www.sphinx-doc.org/
[tox]: https://tox.readthedocs.io/
[ruff]: https://docs.astral.sh/ruff/
[pre-commit]: https://github.com/pre-commit/pre-commit/
[GitHub Actions]: https://github.com/features/actions/
[Read the Docs]: https://readthedocs.org/
