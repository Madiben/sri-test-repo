# SRI Hash Updater GitHub Action

## Overview
This GitHub Action generates a Subresource Integrity (SRI) hash for JavaScript files and updates `index.html` with the correct integrity attribute. It’s a straightforward solution for ensuring resource integrity.

## Features
- Generates a SHA-256 SRI hash for `main.js`.
- Updates `index.html` with the new SRI hash.
- Commits and pushes changes back to the repo if updates are made.

## Setup and Usage

1. **Add the Workflow**: Place the workflow file in `.github/workflows/update-sri.yml` in your repo.
2. **Include the Python Script**: Ensure your `update_sri.py` script is saved in the `scripts/` folder.

Refer to the `update-sri.yml` and `update_sri.py` files for the exact configurations.

### Permissions
Make sure GitHub Actions has **Read and Write** permissions under **Settings > Actions** in your repo.

## Reusing in CI/CD Pipelines
To use this SRI updater in other CI/CD pipelines, save it as a reusable workflow and reference it in your main CI/CD workflow:

```yaml
jobs:
  sri-update:
    uses: owner/repo-name/.github/workflows/update-sri.yml@main  # Update with your repo details

  build:
    needs: sri-update
    runs-on: ubuntu-latest
```
- **`sri-update` Job**: This job calls the reusable `update-sri.yml` workflow, allowing the SRI Hash Updater to run as part of the overall CI/CD pipeline. Replace `owner/repo-name` with the actual GitHub repository details.
- **`needs: sri-update`**: This condition ensures that the `build` and `deploy` jobs only start after the SRI hash is updated, maintaining the security of linked resources before proceeding to the build and deployment steps.

## Contributions
Pull requests are welcome! Feel free to suggest improvements or new features.

## License
This project is licensed under the MIT License.