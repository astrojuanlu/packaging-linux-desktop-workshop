### 1. Modern library packaging with `uv` and `uv-build`

This is how you create a new project with `uv`.

1. Create a new directory: `mkdir test-app && cd test-app`{{exec}}

2. Initialise the Python project using `uv init`: `uv init --app --package --python $(which python3)`{{exec}}

Some comments:
- `--app` will add a CLI entrypoint to the `[project]` table of `pyproject.toml`,
- `--package` will set up the project to be built as a Python package
  by adding the `[build-system]` table to `pyproject.toml`
- `--python $(which python3)` will set the system Python as the minimum required version
  and use it for the virtual environment.

3. Try the test application: `uv run test-app`{{exec}}

You should see `Hello from test-app!`.

---

uv can handle workspaces, collections of one or more packages (members) that are related.

4. Create a `packages/test-lib` directory: `mkdir -p packages/test-lib && cd packages/test-lib`{{exec}}

5. Initialise a library project: `uv init --lib`{{exec}}

Notice that
- A new library scaffolding was created under `packages/test-lib`, but no new `.venv` or `uv.lock`
- The root `pyproject.toml` now contains a new `[tool.uv.workspace]` table

6. Go back to the root of the project: `cd ../..`{{exec}}

7. Add the local `test-lib` as a dependency: `uv add packages/test-lib/`

Notice that
- `test-lib` was added to `[project.dependencies]`
- `test-lib` was declared as coming from the workspace under `[tool.uv.sources]`

8. Modify `src/test_app/__init__.py` to import and use the `hello` function from the `test_lib` package

9. Check that `uv run test-app`{{exec}} gives exactly the same result
