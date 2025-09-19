#!/bin/bash
REPO="https://github.com/asharayiah/clarity.git"
BRANCH="breakthespell/add-campaign-$(date +%Y%m%d%H%M)"
git clone "$REPO" tmp-clarity-repo
cd tmp-clarity-repo
git checkout -b "$BRANCH"
cp -r ../breakthespell_package_local/* ./
git add -A
git commit -m "Add BreakTheSpell campaign assets"
git push origin "$BRANCH"
echo "Now create PR: gh pr create --title 'Add BreakTheSpell campaign' --body 'Adds multilingual campaign assets' --base main --head $BRANCH"
