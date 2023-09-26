# lib-driver
Python package used to launch chromedriver through selenium

# deploy new version steps
1. change setup version (setup.py)
2. commit and push changes
3. add local tag (git tag <version number>)
4. push tag (git push origin <version number>)

# Import command (to adapt)
pip install git+https://github.com/QuentinMalnatti/<lib_repo>.git@v<version_number>#egg=<lib_name>
