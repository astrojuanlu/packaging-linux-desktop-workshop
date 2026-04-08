### 5. More formats with Briefcase: native packages, AppImage, Flatpak

> Note that Briefcase has limited support for uv,
> so several workarounds are needed.

- Add `briefcase` to the list of development dependencies: `uv add --dev briefcase`{{exec}}
- Convert the current project to the Briefcase template: `uv run briefcase convert`

> You can pick the default for most options,
> but remember to use `org.canonical.test-toga-app` as the Bundle Identifier.

- Rework the local dependency as follows:

```toml
dependencies = [
    # "test-lib"  # NOTE: Briefcase uses pip, so it does not understand uv workspaces
    "test-lib @ file:///home/ubuntu/Projects/Canonical/Developer%20Success/packaging-linux-desktop-workshop/packages/test-lib",
]
```

- Add `toga` to the required Briefcase dependencies:

```
requires = [
    # Add your cross-platform app requirements here
    "toga>=0.5.3",  # NOTE: No way to specify extras in Briefcase
]
```

- **On the graphical session**, test that `uv run briefcase dev` launches the application.

---

First, let's package the application as a Debian `.deb` package:

- Create an empty `CHANGELOG` file: `touch changelog`
- Package the application `uv run briefcase package`{{exec}}
- Install the newly created `.deb`: `sudo apt install ./dist/test-app_0.0.1-1~ubuntu-noble_amd64.deb`{{exec}}
- **On the graphical session**, test that `test-app` launches the application

Success!

---

> **Warning:** The Flatpak integration may have some unaddressed bugs.

Next, let's try Flatpak:

- Install the necessary tools: `sudo apt install -y flatpak-builder`{{exec}}
- Package the application: `uv run briefcase package linux flatpak`{{exec}}

> This will take a while.

- Install the newly created Flatpak: `flatpak install ./dist/Test_App-0.0.1-x86_64.flatpak`{{exec}}
- Run the app: `flatpak run org.canonical.test-toga-app`{{exec}}
