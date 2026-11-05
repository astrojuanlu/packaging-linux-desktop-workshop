### 2. Compiled code, the easy way: Rust and maturin

Now you will rewrite the library code so that it uses Rust instead.

- Remove the contents of `packages/test-lib`: `cd ~/test-app && rm -rv ./packages/test-lib/`{{exec}}
- Initialise a new library with `maturin`: `cd ~/test-app/packages && uvx maturin new -b pyo3 --src test-lib`{{exec}}

> Some comments:
> - `-b pyo3` will use PyO3 to generate the Rust bindings
> - `--src test-lib` will scaffold the library in the `test-lib` directory

- Test that the library code works: `cd ~/test-app/packages/test-lib && uv run python -c "from test_lib import sum_as_string as s; print(s(2, 3))"`{{exec}}

You should see `5`.

Notice that the actual code comes from `src/lib.rs`, which is written in Rust!

Now, let's restore the `hello` function that existed in `test-lib`. For that, edit `src/lib.rs` so it looks as follows:

```rust
#[pymodule]
mod test_lib {
    use pyo3::prelude::*;

    /// Returns a salutation string.
    #[pyfunction]
    fn hello() -> PyResult<String> {
        Ok("Hello from Rust 🦀".to_string())
    }
}
```

And add this to your `packages/test-lib/pyproject.toml` for convenience:

```
[tool.uv]
# Rebuild package when any rust files change
cache-keys = [{file = "pyproject.toml"}, {file = "rust/Cargo.toml"}, {file = "**/*.rs"}]
```

After the change, `cd ~/test-app && uv run test-app` should print "Hello from Rust 🦀".

**Exercise:** Tweak the directory structure so it follows https://www.maturin.rs/project_layout.html#alternate-python-source-directory-src-layout.
You will need to add an `__init__.py` with the contents described in https://www.maturin.rs/project_layout.html#pure-rust-project
as well as the `hello` function that existed earlier. The behaviour of the code should be exactly the same.
