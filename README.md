### README: SRI Hash Updater GitHub Action

#### Overview
This GitHub Action automatically generates a Subresource Integrity (SRI) hash for JavaScript files and updates the `index.html` file with the correct `integrity` attribute. Designed for developers looking to improve security by ensuring that the resources are delivered without being tampered with.

#### Features
- Automatically generates a SHA-256 hash for `main.js`.
- Updates `index.html` with the correct SRI hash.
- Commits and pushes the changes back to the repository.

#### Usage

1. **Setup**: Add this action to your `.github/workflows/` directory.

2. **Example Workflow**:
   ```yaml
   name: Update SRI Hash

   on:
     push:
       paths:
         - 'src/proj/main.js'

   jobs:
     update-sri:
       runs-on: ubuntu-latest
       steps:
         - name: Checkout repository
           uses: actions/checkout@v3

         - name: Set up Python
           uses: actions/setup-python@v4
           with:
             python-version: '3.x'

         - name: Run SRI Update Script
           run: python scripts/update-sri.py  # Path to your script

         - name: Commit and push changes
           run: |
             git config --global user.name 'github-actions[bot]'
             git config --global user.email 'github-actions[bot]@users.noreply.github.com'
             git add src/proj/index.html
             git commit -m 'Update SRI hash for main.js'
             git push
           env:
             GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
   ```

3. **Python Script**:
   Ensure you have the `update_sri.py` script inside your `scripts/` folder.

4. **Permissions**:
   Ensure your repository has **Read and Write** permissions enabled for GitHub Actions under `Settings` > `Actions`.

#### How It Works
This workflow triggers when changes are made to `main.js`, generates a new SRI hash, updates the `index.html` file, and pushes the changes back to the repository.

#### Contributions
Feel free to contribute via pull requests!

#### License
This project is licensed under the MIT License.
