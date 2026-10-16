# Contribute to this repository

The public repository is [DustinPetersen/built-world-challenge-starter-kit](https://github.com/DustinPetersen/built-world-challenge-starter-kit).

## Local development

```sh
git clone https://github.com/DustinPetersen/built-world-challenge-starter-kit.git
cd built-world-challenge-starter-kit
python scripts/verify_release.py
```

Create a branch for changes, follow CONTRIBUTING.md, and submit a pull request. Keep sponsor material and credentials outside this public repository. The GitHub Actions workflow runs the offline examples and release checks.

After changing tracked content, regenerate the file manifest with `python scripts/update_manifest.py`, then run `python scripts/verify_release.py`. The manifest excludes itself, Git internals and Python caches.
