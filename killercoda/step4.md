### 4. Packaging for Ubuntu with Snapcraft

- Install `snapcraft`: `sudo snap install snapcraft --classic`{{exec}}
- Initialise the metadata: `cd ~/test-app && snapcraft init`{{exec}}

> Notice that a `snap/snapcraft.yaml` file was created with some dummy metadata.

- Run `snapcraft pack`{{exec}}

> This will install [LXD](https://canonical.com/lxd) and bootstrap the build environment. 
> The result will be an empty snap, there's nothing inside it!
> You still have to tweak the `snapcraft.yaml` metadata.

---

Let's package the CLI part first.

- Modify the [`parts`](https://documentation.ubuntu.com/snapcraft/stable/explanation/parts/) object to look as follows:

```yaml
parts:
  test-app:
    plugin: uv
    source: .
    build-snaps:
      - astral-uv
```

> Some comments:
> - `plugin: uv` defines how the code is going to be built,
>   `snapcraft plugins` shows a complete list of plugins
> - `source: .` defines where the source code comes from (current directory)
> - `build-snaps:` defines which snaps need to be installed for building the source,
>   including `uv` itself
>
> Snapcraft builds the snap in a series of
> [stages](https://documentation.ubuntu.com/snapcraft/stable/explanation/parts-lifecycle/).
> You can invoke each of them individually with the appropriate command,
> optionally specify which part to focus on.
> For example: `snapcraft pull test-app -v`{{exec}}.

- Add the following [`app`](https://documentation.ubuntu.com/snapcraft/stable/reference/project-file/anatomy-of-snapcraft-yaml/#apps):

```yaml
apps:
  test-app:
    command: bin/test-app
```

- Pack the snap again: `snapcraft pack`{{exec}}
- Install the snap: `sudo snap install ./test-app_0.1_amd64.snap --devmode`

> The `--devmode` flag is needed
> because of the `confinement: devmode` key in `snapcraft.yaml`.

- Run `test-app`{{exec}}

You should see some terminal output.

---

And now, let's package the GUI application as well.

- Add another part corresponding to `test-app-gui`:

```yaml
apps:
  test-app:
    ...
  test-app-gui:
    command: bin/test-app-gui
```

- Tweak the building of the `test-app` part
  so that optional dependencies are also included (needed for `toga`):

```yaml
parts:
  test-app:
    ...
    uv-extras:
      - gui
```

- Add the necessary system libraries to compile the dependencies from source:

```yaml
parts:
  test-app:
    ...
    build-packages:
      - libcairo2-dev
      - libgirepository-2.0-dev
```

- Stage the necessary system libraries that need to be present in the final package:

```yaml
parts:
  test-app:
    ...
    stage-packages:
      - libfontconfig1
      - libgirepository-2.0-0
```
