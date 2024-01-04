set WP_PASSWORD=""

python %~dp0m2w.py %*

git add .
git commit -m "commit"
git push