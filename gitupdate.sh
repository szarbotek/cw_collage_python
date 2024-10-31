#!/bin/bash
echo "Give folder to send to github.com: "
read folder_name
dictionary_path=$(dirname "$(realpath "$0")")
file_path="$dictionary_path/$folder_name"
comm_git="D:/szarbotek/git/bin/git.exe"

if [ -d "$file_path" ]; then
    echo "Folder exist: $file_path"

    # git --version
    # git init
    # git add "./*"
    # git commit -m "update resposible"
    # # git branch -M main
    # # git remote add origin https://github.com/szarbotek/cw_collage_python.git
    # git push push -u origin main

    "$comm_git" --version
    "$comm_git" init
    "$comm_git"  add "./*"
    "$comm_git" commit -m "update resposible"
    "$comm_git" branch -M main
    "$comm_git" remote add origin https://github.com/szarbotek/cw_collage_python.git
    "$comm_git" push push --force origin main

    # echo "[add] work"
    # "$comm_git"  commit -m "update resposible"
    # echo "[commit] work"
    # "$comm_git"  branch -M main
    # echo "[branch] work"
    # "$comm_git" remote add origin https://github.com/szarbotek/cw_collage_python.git
    # echo "[remote.add] work"
    # "$comm_git"  push -u origin main
    # echo "[push] work"
else
    echo "Folder not exist: $file_path"
fi