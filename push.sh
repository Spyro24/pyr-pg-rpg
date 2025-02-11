#!/bin/bash
rm README.html
rm ./logs/*
markdown-it README.md > README.html
git add *
git commit
git push
